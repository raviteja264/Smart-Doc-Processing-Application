from fastapi import APIRouter
from datetime import datetime

router = APIRouter(tags=["Status"])

@router.get("/status", status_code=200)
async def api_status():
    """
    Endpoint to check the status of the API.
    """
    return {
        "status": "running",
        "message": "Smart Doc Processing API is up and running!",
        "timestamp": datetime.now().isoformat()
    }