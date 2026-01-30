from core.llm import LLMService

def test():
    print("Initializing LLM Service...")
    service = LLMService()
    service.load_model()
    
    samples = [
        "The app keeps crashing after the last update.",
        "I was charged twice this month.",
        "Overall the idea is good."
    ]
    
    print("\nStarting Inference Tests...")
    for s in samples:
        topic = service.analyze_sentence(s)
        print(f"Sample: '{s}' -> Topic: '{topic}'")

if __name__ == "__main__":
    test()
