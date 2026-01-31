from typing import List
from app.models.sentence import Sentence
from app.models.topic import Topic
from app.schemas.analyze import AnalyzeRequest, AnalyzeResponse, SentenceResult
from app.services.llm_service import LLMService
from app.utils.text_processing import split_into_sentences
from app.core.logging import get_logger

logger = get_logger(__name__)


class ReviewAnalysisService:
    """
    Service for analyzing customer reviews.
    Orchestrates text processing and LLM analysis.
    """
    
    def __init__(self, llm_service: LLMService):
        """
        Initialize review analysis service.
        
        Args:
            llm_service: LLM service for topic classification
        """
        self.llm_service = llm_service
    
    async def analyze_review(self, request: AnalyzeRequest) -> AnalyzeResponse:
        """
        Analyze a customer review and classify sentences by topic.
        
        Args:
            request: Analysis request containing review text
            
        Returns:
            Analysis response with classified sentences
        """
        logger.info(f"Analyzing review with {len(request.text)} characters")
        
        # Step 1: Split into sentences
        sentence_texts = split_into_sentences(request.text)
        logger.debug(f"Split into {len(sentence_texts)} sentences")
        
        # Step 2: Analyze each sentence
        sentences = await self._analyze_sentences(sentence_texts)
        
        # Step 3: Convert to response schema
        response = self._build_response(sentences)
        
        logger.info(f"Analysis complete: {len(response.sentences)} sentences classified")
        return response
    
    async def _analyze_sentences(self, sentence_texts: List[str]) -> List[Sentence]:
        """
        Analyze multiple sentences and classify their topics.
        
        Args:
            sentence_texts: List of sentence strings
            
        Returns:
            List of Sentence domain entities
        """
        sentences: List[Sentence] = []
        
        for index, text in enumerate(sentence_texts):
            topic = await self.llm_service.analyze_sentence(text)
            sentence = Sentence(index=index, text=text, topic=topic)
            sentences.append(sentence)
        
        return sentences
    
    def _build_response(self, sentences: List[Sentence]) -> AnalyzeResponse:
        """
        Convert domain entities to API response schema.
        
        Args:
            sentences: List of Sentence domain entities
            
        Returns:
            AnalyzeResponse schema
        """
        sentence_results = [
            SentenceResult(
                index=sentence.index,
                text=sentence.text,
                topic=sentence.topic_name
            )
            for sentence in sentences
        ]
        
        return AnalyzeResponse(sentences=sentence_results)
