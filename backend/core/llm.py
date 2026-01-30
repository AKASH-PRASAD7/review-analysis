from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import logging

# Suppress warnings
logging.getLogger("transformers").setLevel(logging.ERROR)

class LLMService:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.model_name = "google/flan-t5-small"

    def load_model(self):
        if self.model is not None:
            return

        print(f"Loading model {self.model_name}...")
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None

    def analyze_sentence(self, text: str) -> str:
        # Fallback Keywords (Hybrid approach for reliability on small model)
        lower_text = text.lower()
        if "crash" in lower_text or "slow" in lower_text or "lag" in lower_text:
            return "Performance"
        if "bill" in lower_text or "charg" in lower_text or "refund" in lower_text:
            return "Billing"
        if "support" in lower_text or "help" in lower_text or "service" in lower_text:
            return "Support"
        if "login" in lower_text or "password" in lower_text or "sign in" in lower_text:
            return "Account"
        
        if self.model is None:
            return "Other"

        # Few-shot Prompting for T5
        prompt = f"""Classify review sentences into: Billing, Performance, Support, UX, Account, Other.

Input: The screen is frozen.
Topic: Performance
Input: I was charged double.
Topic: Billing
Input: The button is hard to find.
Topic: UX
Input: {text}
Topic:"""

        try:
            inputs = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
            outputs = self.model.generate(**inputs, max_new_tokens=10)
            output_text = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
            
            print(f"DEBUG: Input='{text}' | Model Output='{output_text}'")
            return self._validate_topic(output_text)
        except Exception as e:
            print(f"Inference error: {e}")
            return "Other"

    def _validate_topic(self, topic: str) -> str:
        allowed = ["Billing", "Performance", "Support", "UX", "Account", "Other"]
        clean_topic = topic.replace(".", "").strip()
        
        for a in allowed:
            if a.lower() == clean_topic.lower():
                return a
        
        for a in allowed:
            if a.lower() in clean_topic.lower():
                return a
                
        return "Other"

llm_service = LLMService()
