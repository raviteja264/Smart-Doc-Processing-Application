from fastapi import APIRouter

router = APIRouter(tags=["Info"])

@router.get("/info", status_code=200)
async def app_info():
    """
    Endpoint to provide basic information about the application.
    """
    return {
        "app_name": "Smart Doc Processing API",
        "version": "1.0",
        "description": "API for processing and managing smart documents.",
        "maintainer_email": "tejarockz100@gmail.com"
    }