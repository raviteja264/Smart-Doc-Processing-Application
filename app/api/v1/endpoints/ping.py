from fastapi import APIRouter

router = APIRouter(prefix="/ping", tags=["ping"])

@router.get("/ping", status_code=200)
async def ping():
    return {"message": "pong"}