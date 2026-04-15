from fastapi import FastAPI
from app.api.v1.endpoints import health, info, status, ping
from app.core.logger import setup_logging
from app.core.config import settings

# Setup logging
setup_logging(settings.log_level)

app = FastAPI(title="Smart Doc Processing API", version="1.0")

# Register routers
app.include_router(health.router, prefix="/api/v1")
app.include_router(info.router, prefix="/api/v1")
app.include_router(status.router, prefix="/api/v1")
app.include_router(ping.router, prefix="/api/v1")