from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

from app.core.config import get_settings
from app.core.logging import setup_logging, get_logger
from app.core.exceptions import ReviewAnalysisException, ModelNotLoadedException
from app.api.v1.api_router import api_router
from app.api.v1.dependencies import get_llm_service

# Setup logging
setup_logging()
logger = get_logger(__name__)

# Get settings
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.
    Handles startup and shutdown events.
    """
    # Startup
    logger.info("Starting application...")
    logger.info(f"App: {settings.app_name} v{settings.app_version}")
    
    # Load LLM model
    try:
        llm_service = get_llm_service()
        llm_service.load_model()
        logger.info("LLM model loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load LLM model: {e}")
        logger.warning("Application will continue with keyword-based classification")
    
    yield
    
    # Shutdown
    logger.info("Shutting down application...")


# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API for analyzing customer reviews and classifying sentences by topic",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)


# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allow_methods,
    allow_headers=settings.cors_allow_headers,
)


# Global Exception Handlers

@app.exception_handler(ReviewAnalysisException)
async def review_analysis_exception_handler(
    request: Request,
    exc: ReviewAnalysisException
) -> JSONResponse:
    """Handle custom review analysis exceptions."""
    logger.error(f"Review analysis error: {exc.message}")
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": exc.message,
            "details": exc.details
        }
    )


@app.exception_handler(ModelNotLoadedException)
async def model_not_loaded_exception_handler(
    request: Request,
    exc: ModelNotLoadedException
) -> JSONResponse:
    """Handle model not loaded exceptions."""
    logger.error(f"Model not loaded: {exc.message}")
    
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={
            "message": "LLM model not available, using fallback classification",
            "details": exc.details
        }
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
) -> JSONResponse:
    """Handle Pydantic validation errors."""
    logger.warning(f"Validation error: {exc.errors()}")
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "message": "Validation error",
            "details": exc.errors()
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(
    request: Request,
    exc: Exception
) -> JSONResponse:
    """Handle all other exceptions."""
    logger.exception(f"Unhandled exception: {str(exc)}")
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": "Internal server error",
            "details": str(exc) if settings.debug else None
        }
    )


# Include API routers
app.include_router(api_router, prefix=settings.api_v1_prefix)


# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information."""
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "docs": "/docs",
        "health": f"{settings.api_v1_prefix}/health"
    }
