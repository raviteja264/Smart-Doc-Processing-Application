from fastapi import APIRouter, Depends
from app.services.status_service import StatusService
from app.api.dependencies import get_status_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Status"])

@router.get("/status", status_code=200)
async def api_status(service: StatusService = Depends(get_status_service)):
    """
    Endpoint to check the status of the API.
    """
    logger.info("Status endpoint triggered")
    return service.get_status()