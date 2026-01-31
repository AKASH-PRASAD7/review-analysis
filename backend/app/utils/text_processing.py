import re
from typing import List


def split_into_sentences(text: str) -> List[str]:
    """
    Split text into sentences using punctuation rules.
    
    Args:
        text: Input text to split
        
    Returns:
        List of sentence strings
        
    Examples:
        >>> split_into_sentences("Hello world. How are you?")
        ['Hello world.', 'How are you?']
    """
    # Split after . ! ? followed by whitespace
    # Pattern: (?<=[.!?])\s+
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Filter out empty strings and strip whitespace
    return [s.strip() for s in sentences if s.strip()]
