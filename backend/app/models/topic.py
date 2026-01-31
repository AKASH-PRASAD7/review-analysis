from enum import Enum
from typing import List


class Topic(str, Enum):
    """
    Enumeration of possible review topics.
    Inherits from str for JSON serialization compatibility.
    """
    
    BILLING = "Billing"
    PERFORMANCE = "Performance"
    SUPPORT = "Support"
    UX = "UX"
    ACCOUNT = "Account"
    OTHER = "Other"
    
    @classmethod
    def from_string(cls, value: str) -> "Topic":
        """
        Convert a string to a Topic enum, with fuzzy matching.
        
        Args:
            value: String representation of the topic
            
        Returns:
            Matching Topic enum value, defaults to OTHER if no match
        """
        clean_value = value.replace(".", "").strip()
        
        # Exact match
        for topic in cls:
            if topic.value.lower() == clean_value.lower():
                return topic
        
        # Partial match
        for topic in cls:
            if topic.value.lower() in clean_value.lower():
                return topic
        
        return cls.OTHER
    
    @classmethod
    def all_values(cls) -> List[str]:
        """Get all topic values as a list of strings."""
        return [topic.value for topic in cls]
    
    @classmethod
    def detect_from_keywords(cls, text: str) -> "Topic":
        """
        Detect topic based on keyword matching.
        Fallback method when LLM is unavailable.
        
        Args:
            text: Text to analyze
            
        Returns:
            Detected Topic
        """
        lower_text = text.lower()
        
        # Performance keywords
        if any(keyword in lower_text for keyword in ["crash", "slow", "lag", "freeze", "hang", "performance"]):
            return cls.PERFORMANCE
        
        # Billing keywords
        if any(keyword in lower_text for keyword in ["bill", "charg", "refund", "payment", "price", "cost"]):
            return cls.BILLING
        
        # Support keywords
        if any(keyword in lower_text for keyword in ["support", "help", "service", "assist", "response"]):
            return cls.SUPPORT
        
        # Account keywords
        if any(keyword in lower_text for keyword in ["login", "password", "sign in", "account", "auth"]):
            return cls.ACCOUNT
        
        # UX keywords
        if any(keyword in lower_text for keyword in ["button", "ui", "interface", "design", "confusing", "hard to find"]):
            return cls.UX
        
        return cls.OTHER
