from app.services.health_service import HealthService
from app.services.info_service import InfoService
from app.services.ping_service import PingService
from app.services.status_service import StatusService

def get_health_service() -> HealthService:
    return HealthService()

def get_info_service() -> InfoService:
    return InfoService()

def get_ping_service() -> PingService:
    return PingService()

def get_status_service() -> StatusService:
    return StatusService()
