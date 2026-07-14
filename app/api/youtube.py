from fastapi import APIRouter
from app.services.youtube import YouTubeService

router = APIRouter()
service = YouTubeService()

@router.get("/search")
def search(q: str):
    return {
        "success": True,
        "data": service.search(q)
    }

@router.get("/stream/{video_id}")
def stream(video_id: str):
    return {
        "success": True,
        "data": service.resolve(video_id)
    }