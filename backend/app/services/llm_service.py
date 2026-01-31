from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from typing import Optional
from app.core.config import Settings
from app.core.logging import get_logger
from app.core.exceptions import ModelNotLoadedException, AnalysisException
from app.models.topic import Topic

logger = get_logger(__name__)


class LLMService:
    """
    Service for LLM-based text analysis.
    Handles model loading, inference, and topic classification.
    """
    
    def __init__(self, settings: Settings):
        """
        Initialize LLM service.
        
        Args:
            settings: Application settings containing model configuration
        """
        self.settings = settings
        self.model: Optional[AutoModelForSeq2SeqLM] = None
        self.tokenizer: Optional[AutoTokenizer] = None
        self._model_loaded = False
    
    def load_model(self) -> None:
        """
        Load the LLM model and tokenizer.
        Idempotent - safe to call multiple times.
        
        Raises:
            ModelNotLoadedException: If model loading fails
        """
        if self._model_loaded:
            logger.info("Model already loaded, skipping")
            return
        
        logger.info(f"Loading model: {self.settings.model_name}")
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.settings.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.settings.model_name)
            self._model_loaded = True
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise ModelNotLoadedException(
                f"Failed to load model {self.settings.model_name}",
                details=str(e)
            )
    
    def is_model_loaded(self) -> bool:
        """Check if the model is loaded and ready."""
        return self._model_loaded and self.model is not None
    
    async def analyze_sentence(self, text: str) -> Topic:
        """
        Analyze a sentence and classify its topic.
        Uses hybrid approach: keyword matching + LLM inference.
        
        Args:
            text: Sentence text to analyze
            
        Returns:
            Classified Topic
            
        Raises:
            AnalysisException: If analysis fails
        """
        # Try keyword-based detection first (fast fallback)
        keyword_topic = Topic.detect_from_keywords(text)
        
        # If model not loaded, use keyword detection
        if not self.is_model_loaded():
            logger.warning("Model not loaded, using keyword-based detection")
            return keyword_topic
        
        # Use LLM for more accurate classification
        try:
            topic_str = await self._run_inference(text)
            llm_topic = Topic.from_string(topic_str)
            
            logger.debug(f"Analyzed: '{text[:50]}...' -> {llm_topic.value}")
            return llm_topic
            
        except Exception as e:
            logger.error(f"LLM inference failed: {e}, falling back to keywords")
            return keyword_topic
    
    async def _run_inference(self, text: str) -> str:
        """
        Run LLM inference on the text.
        
        Args:
            text: Input text
            
        Returns:
            Raw model output
            
        Raises:
            AnalysisException: If inference fails
        """
        if not self.is_model_loaded():
            raise ModelNotLoadedException("Model must be loaded before inference")
        
        # Few-shot prompting for better results
        prompt = self._build_prompt(text)
        
        try:
            inputs = self.tokenizer(
                prompt,
                return_tensors="pt",
                max_length=self.settings.max_tokens,
                truncation=True
            )
            
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=self.settings.max_new_tokens
            )
            
            output_text = self.tokenizer.batch_decode(
                outputs,
                skip_special_tokens=True
            )[0]
            
            return output_text
            
        except Exception as e:
            raise AnalysisException(
                "LLM inference failed",
                details=str(e)
            )
    
    def _build_prompt(self, text: str) -> str:
        """
        Build few-shot prompt for topic classification.
        
        Args:
            text: Text to classify
            
        Returns:
            Formatted prompt
        """
        topics_list = ", ".join(Topic.all_values())
        
        return f"""Classify review sentences into: {topics_list}.

Input: The screen is frozen.
Topic: Performance
Input: I was charged double.
Topic: Billing
Input: The button is hard to find.
Topic: UX
Input: {text}
Topic:"""
