from fastapi import APIRouter, Depends
from app.services.health_service import HealthService

router = APIRouter(tags=["Health"])

def get_health_service() -> HealthService:
    return HealthService()

@router.get("/health", status_code=200)
async def health_check(service: HealthService = Depends(get_health_service)):
    """
    Health check endpoint to verify that the API is running.
    """
    return service.check_health()
