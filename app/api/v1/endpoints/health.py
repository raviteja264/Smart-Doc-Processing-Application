from fastapi import APIRouter
from app.core.config import settings

router = APIRouter(tags=["Health"])

@router.get("/health", status_code=200)
async def health_check():
    """
    Health check endpoint to verify that the API is running.
    """
    return {
        "status": "Ok",
        "app_name": settings.app_name,
        "env": settings.env
    }
