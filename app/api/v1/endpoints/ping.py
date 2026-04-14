from fastapi import APIRouter, Depends
from app.services.ping_service import PingService

router = APIRouter(tags=["ping"])

def get_ping_service() -> PingService:
    return PingService()

@router.get("/ping", status_code=200)
async def ping(service: PingService = Depends(get_ping_service)):
    """
    Endpoint to check if the API is responsive.

    """
    return service.get_ping()