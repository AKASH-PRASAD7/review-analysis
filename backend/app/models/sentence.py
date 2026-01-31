from dataclasses import dataclass
from app.models.topic import Topic


@dataclass(frozen=True)
class Sentence:
    """
    Domain entity representing an analyzed sentence.
    Immutable dataclass with no framework dependencies.
    """
    
    index: int
    text: str
    topic: Topic
    
    def __post_init__(self):
        """Validate sentence data after initialization."""
        if self.index < 0:
            raise ValueError("Sentence index must be non-negative")
        if not self.text.strip():
            raise ValueError("Sentence text cannot be empty")
    
    @property
    def topic_name(self) -> str:
        """Get the topic as a string value."""
        return self.topic.value
