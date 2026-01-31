from functools import lru_cache
from fastapi import Depends
from app.core.config import get_settings, Settings
from app.services.llm_service import LLMService
from app.services.review_analysis_service import ReviewAnalysisService


# Singleton instances
_llm_service: LLMService | None = None
_review_service: ReviewAnalysisService | None = None


def get_settings_dependency() -> Settings:
    """Dependency for getting application settings."""
    return get_settings()


def get_llm_service() -> LLMService:
    """
    Dependency for getting LLM service instance.
    Creates singleton instance on first call.
    """
    global _llm_service
    
    if _llm_service is None:
        settings = get_settings()
        _llm_service = LLMService(settings)
    
    return _llm_service


def get_review_service(
    llm_service: LLMService = Depends(get_llm_service)
) -> ReviewAnalysisService:
    """
    Dependency for getting review analysis service.
    Creates singleton instance on first call.
    
    Args:
        llm_service: Optional LLM service (injected by FastAPI)
    """
    global _review_service
    
    if _review_service is None:
        if llm_service is None:
            llm_service = get_llm_service()
        _review_service = ReviewAnalysisService(llm_service)
    
    return _review_service
