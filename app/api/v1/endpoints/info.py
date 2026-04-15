from fastapi import APIRouter, Depends
from app.services.info_service import InfoService
from app.api.dependencies import get_info_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Info"])

@router.get("/info", status_code=200)
async def app_info(service: InfoService = Depends(get_info_service)):
    """
    Endpoint to provide basic information about the application.
    """
    logger.info("App info endpoint triggered")
    return service.get_app_info()