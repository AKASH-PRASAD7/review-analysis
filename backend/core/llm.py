from transformers import pipeline
import logging

# Suppress warnings
logging.getLogger("transformers").setLevel(logging.ERROR)

class LLMService:
    def __init__(self):
        self.classifier = None
        self.model_name = "google/flan-t5-small"

    def load_model(self):
        if self.classifier is not None:
            return

        print(f"Loading model {self.model_name}...")
        try:
            # We use text2text-generation for FLAN-T5
            self.classifier = pipeline(
                "text2text-generation", 
                model=self.model_name, 
                max_length=64
            )
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.classifier = None

    def analyze_sentence(self, text: str) -> str:
        if self.classifier is None:
            # Fallback if model failed to load
            return "Other"

        # FLAN-T5 prompt engineering
        # We need a prompt that forces a specific output.
        prompt = f"""Classify this sentence into one category: Billing, Performance, Support, UX, Account, or Other.

Sentence: {text}
Category:"""

        try:
            result = self.classifier(prompt)
            # result is [{'generated_text': '...'}]
            output = result[0]['generated_text'].strip()
            
            # Clean up output
            return self._validate_topic(output)
        except Exception as e:
            print(f"Inference error: {e}")
            return "Other"

    def _validate_topic(self, topic: str) -> str:
        allowed = ["Billing", "Performance", "Support", "UX", "Account", "Other"]
        # Simple cleanup
        clean_topic = topic.replace(".", "").strip()
        
        for a in allowed:
            if a.lower() in clean_topic.lower():
                return a
        return "Other"

llm_service = LLMService()
