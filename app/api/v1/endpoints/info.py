from fastapi import APIRouter, Depends
from app.services.info_service import InfoService

router = APIRouter(tags=["Info"])

def get_info_service() -> InfoService:
    return InfoService()

@router.get("/info", status_code=200)
async def app_info(service: InfoService = Depends(get_info_service)):
    """
    Endpoint to provide basic information about the application.
    """
    return service.get_app_info()