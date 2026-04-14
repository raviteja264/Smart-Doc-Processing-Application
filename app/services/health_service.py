from app.core.config import settings

class HealthService:
    def check_health(self) -> dict:
        return {
            "status": "Ok",
            "app_name": settings.app_name,
            "env": settings.env
        }