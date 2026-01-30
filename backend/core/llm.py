import os
import json
import re
from typing import Optional

# Try importing Llama, handle if missing for lightweight setups/dev without deps
try:
    from llama_cpp import Llama
except ImportError:
    Llama = None

class LLMService:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.llm: Optional[Llama] = None

    def load_model(self):
        if self.llm is not None:
            return

        if Llama is None:
            print("llama-cpp-python not installed. Running in mock mode.")
            return

        if not os.path.exists(self.model_path):
            print(f"Model file not found at {self.model_path}. Running in mock mode.")
            return

        try:
            # Context window small for efficiency
            self.llm = Llama(
                model_path=self.model_path,
                n_ctx=512,
                verbose=False,
                n_gpu_layers=0 # Run on CPU for free tier compat
            )
            print(f"Model loaded from {self.model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.llm = None

    def analyze_sentence(self, text: str) -> str:
        # Mock behavior if no model loaded
        if self.llm is None:
            return self._mock_classify(text)

        # Simple prompt
        prompt = f"""Classify the sentence into exactly one of these topics: Billing, Performance, Support, UX, Account, Other.
Return JSON format: {{"topic": "YourTopic"}}

Sentence: "{text}"
JSON:"""

        try:
            # Generate
            output = self.llm(
                prompt,
                max_tokens=32,
                stop=["\n", "Sentence:"],
                temperature=0.0
            )
            response_text = output['choices'][0]['text'].strip()
            
            # Simple JSON extraction
            match = re.search(r'\{.*?\}', response_text)
            if match:
                data = json.loads(match.group(0))
                topic = data.get("topic", "Other")
                return self._validate_topic(topic)
            return "Other"
        except Exception as e:
            print(f"Inference error: {e}")
            return "Other"

    def _validate_topic(self, topic: str) -> str:
        allowed = ["Billing", "Performance", "Support", "UX", "Account", "Other"]
        # Case insensitive check
        for a in allowed:
            if a.lower() == topic.lower():
                return a
        return "Other"

    def _mock_classify(self, text: str) -> str:
        # Simple keywords for testing without model
        lower = text.lower()
        if "crash" in lower or "slow" in lower: return "Performance"
        if "charge" in lower or "money" in lower: return "Billing"
        if "help" in lower or "support" in lower: return "Support"
        if "login" in lower or "account" in lower: return "Account"
        if "ugly" in lower or "button" in lower: return "UX"
        return "Other"

# Configure path
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models", "model.gguf")
llm_service = LLMService(MODEL_PATH)
