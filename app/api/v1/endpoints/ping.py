from fastapi import APIRouter, Depends
from app.services.ping_service import PingService
from app.api.dependencies import get_ping_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter(tags=["ping"])

@router.get("/ping", status_code=200)
async def ping(service: PingService = Depends(get_ping_service)):
    """
    Endpoint to check if the API is responsive.

    """
    logger.info("Ping endpoint triggered")
    return service.get_ping()