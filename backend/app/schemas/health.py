from pydantic import BaseModel, Field, ConfigDict


class HealthResponse(BaseModel):
    """Health check response model."""
    
    status: str = Field(..., description="Overall API status")
    model_loaded: bool = Field(..., description="Whether the LLM model is loaded")
    model_name: str = Field(..., description="Name of the loaded model")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "ok",
                "model_loaded": True,
                "model_name": "google/flan-t5-small"
            }
        }
    )
