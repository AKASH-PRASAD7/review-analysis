from fastapi import APIRouter, Depends, status
from app.schemas.health import HealthResponse
from app.services.llm_service import LLMService
from app.api.v1.dependencies import get_llm_service, get_settings_dependency
from app.core.config import Settings

router = APIRouter(prefix="/health", tags=["Health"])


@router.get(
    "",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Check API and model health status"
)
async def health_check(
    llm_service: LLMService = Depends(get_llm_service),
    settings: Settings = Depends(get_settings_dependency)
) -> HealthResponse:
    """
    Health check endpoint.
    
    Returns:
    - **status**: Overall API status
    - **model_loaded**: Whether the LLM model is loaded
    - **model_name**: Name of the loaded model
    """
    return HealthResponse(
        status="ok",
        model_loaded=llm_service.is_model_loaded(),
        model_name=settings.model_name
    )
