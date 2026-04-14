from fastapi import APIRouter, Depends
from app.services.status_service import StatusService

router = APIRouter(tags=["Status"])

def get_status_service() -> StatusService:
    return StatusService()

@router.get("/status", status_code=200)
async def api_status(service: StatusService = Depends(get_status_service)):
    """
    Endpoint to check the status of the API.
    """
    return service.get_status()