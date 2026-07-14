from fastapi import FastAPI
from app.api.youtube import router as youtube_router

app = FastAPI(
    title="Karaoke Youtube Service",
    version="1.0.0"
)

app.include_router(
    youtube_router,
    prefix="/youtube",
    tags=["Youtube"]
)

@app.get("/")
def root():
    return {
        "service": "karaoke-youtube-service",
        "status": "running"
    }