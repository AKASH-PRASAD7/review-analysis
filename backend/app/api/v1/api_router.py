from fastapi import APIRouter
from app.api.v1.routers import analyze, health

api_router = APIRouter()

# Include all v1 routers
api_router.include_router(health.router)
api_router.include_router(analyze.router)
