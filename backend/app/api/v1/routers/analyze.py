from fastapi import APIRouter, Depends, status
from app.schemas.analyze import AnalyzeRequest, AnalyzeResponse
from app.services.review_analysis_service import ReviewAnalysisService
from app.api.v1.dependencies import get_review_service
from app.core.logging import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/analyze", tags=["Analysis"])


@router.post(
    "",
    response_model=AnalyzeResponse,
    status_code=status.HTTP_200_OK,
    summary="Analyze Customer Review",
    description="Analyze a customer review and classify sentences by topic",
    response_description="List of sentences with classified topics"
)
async def analyze_review(
    request: AnalyzeRequest,
    service: ReviewAnalysisService = Depends(get_review_service)
) -> AnalyzeResponse:
    """
    Analyze a customer review.
    
    - **text**: Customer review text to analyze
    
    Returns a list of sentences with their classified topics:
    - Billing
    - Performance
    - Support
    - UX
    - Account
    - Other
    """
    logger.info("Received analyze request")
    response = await service.analyze_review(request)
    return response
