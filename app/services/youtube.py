from app.providers.youtube import YouTubeProvider

CHANNEL_LIST = [
    "Capleo",
    "TirtaMedia",
    "KaraokeMusicID",
    "Sing King",
    "karaoke SESH",
    "Karaoke Piano",
    "Just Sing It",
    "Tangga Music Studio"
]

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

            if not self.is_karaoke_channel(channel):
                continue

            thumbnails = (
                item.get("thumbnails")
                or []
            )

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

    def is_karaoke_channel(self, channel: str):
        if not channel:
            return False
        channel = channel.lower()

        return any(
            name.lower() in channel
            for name in CHANNEL_LIST
        )