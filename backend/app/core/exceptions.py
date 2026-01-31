from fastapi import HTTPException, status


class ReviewAnalysisException(Exception):
    """Base exception for review analysis errors."""
    
    def __init__(self, message: str, details: str | None = None):
        self.message = message
        self.details = details
        super().__init__(self.message)


class ModelNotLoadedException(ReviewAnalysisException):
    """Raised when the LLM model is not loaded or failed to load."""
    pass


class AnalysisException(ReviewAnalysisException):
    """Raised when analysis fails for a specific input."""
    pass


class ValidationException(ReviewAnalysisException):
    """Raised when input validation fails."""
    pass


class ConfigurationException(ReviewAnalysisException):
    """Raised when there's a configuration error."""
    pass


def create_http_exception(
    status_code: int,
    message: str,
    details: str | None = None
) -> HTTPException:
    """
    Create a standardized HTTP exception.
    
    Args:
        status_code: HTTP status code
        message: Error message
        details: Optional additional details
        
    Returns:
        HTTPException with structured error response
    """
    detail = {"message": message}
    if details:
        detail["details"] = details
        
    return HTTPException(status_code=status_code, detail=detail)
