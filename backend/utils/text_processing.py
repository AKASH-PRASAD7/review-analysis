import re

def split_into_sentences(text: str) -> list[str]:
    """
    Splits text into sentences using simple punctuation rules.
    """
    # Split by period, exclamation mark, or question mark followed by whitespace or end of string.
    # We keep the punctuation with the sentence.
    # This regex looks for (.!?) followed by space or EOF.
    # It might be improved to handle "Mr." etc, but simple is requested.
    
    # Simple approach: Replace common sentence endings with a unique separator
    # This is a bit naive but works for simple reviews.
    
    # Using regex to find split points.
    # pattern: (?<=[.!?])\s+
    # Split after . ! ? followed by whitespace
    
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]
