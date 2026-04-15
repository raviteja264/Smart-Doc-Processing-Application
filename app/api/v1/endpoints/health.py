from fastapi import APIRouter, Depends
from app.services.health_service import HealthService
from app.api.dependencies import get_health_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Health"])

@router.get("/health", status_code=200)
async def health_check(service: HealthService = Depends(get_health_service)):
    """
    Health check endpoint to verify that the API is running.
    """
    logger.info("Health check triggered")
    return service.check_health()
