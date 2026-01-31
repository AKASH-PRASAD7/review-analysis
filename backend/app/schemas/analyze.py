from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import List


class AnalyzeRequest(BaseModel):
    """Request model for review analysis."""
    
    text: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="Customer review text to analyze",
        examples=["The app crashes frequently. Customer support was helpful."]
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "text": "The app crashes frequently. Customer support was helpful."
            }
        }
    )
    
    @field_validator("text")
    @classmethod
    def validate_text_not_empty(cls, v: str) -> str:
        """Ensure text is not just whitespace."""
        if not v.strip():
            raise ValueError("Text cannot be empty or whitespace only")
        return v.strip()


class SentenceResult(BaseModel):
    """Individual sentence analysis result."""
    
    index: int = Field(..., ge=0, description="Sentence index in the review")
    text: str = Field(..., description="The sentence text")
    topic: str = Field(..., description="Classified topic")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "index": 0,
                "text": "The app crashes frequently.",
                "topic": "Performance"
            }
        }
    )


class AnalyzeResponse(BaseModel):
    """Response model for review analysis."""
    
    sentences: List[SentenceResult] = Field(
        ...,
        description="List of analyzed sentences with topics"
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "sentences": [
                    {
                        "index": 0,
                        "text": "The app crashes frequently.",
                        "topic": "Performance"
                    },
                    {
                        "index": 1,
                        "text": "Customer support was helpful.",
                        "topic": "Support"
                    }
                ]
            }
        }
    )
