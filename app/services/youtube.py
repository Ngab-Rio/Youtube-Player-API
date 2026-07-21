from app.providers.youtube import YouTubeProvider


class YouTubeService:
    def __init__(self):
        self.provider = YouTubeProvider()

    def search(self, query: str):
        items = self.provider.search(query)
        videos = []

        for item in items:
            channel = (
                item.get("channel")
                or item.get("uploader")
                or ""
            )

            thumbnails = item.get("thumbnails") or []

            thumbnail = None
            if thumbnails:
                thumbnail = thumbnails[-1].get("url")

            videos.append({
                "videoId": item.get("id"),
                "title": item.get("title"),
                "channel": channel,
                "thumbnail": thumbnail,
                "duration": item.get("duration"),
                "viewCount": item.get("view_count")
            })

        return videos

    def resolve(self, video_id: str):
        return self.provider.resolve(video_id)