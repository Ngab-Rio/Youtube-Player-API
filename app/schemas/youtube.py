from pydantic import BaseModel

class SearchResponse(BaseModel):
    videoId: str
    title: str | None
    channel: str | None
    duration: int | None
    thumbnail: str | None
    viewCount: int | None