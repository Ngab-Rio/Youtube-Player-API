from yt_dlp import YoutubeDL

class YouTubeProvider:

    SEARCH_OPTIONS = {
        "quiet": True,
        "extract_flat": True
    }

    STREAM_OPTIONS = {
        "quiet": True,
        "no_warnings": True
    }

    def search(self, query: str):
        with YoutubeDL(self.SEARCH_OPTIONS) as ydl:
            result = ydl.extract_info(
                f"ytsearch90:{query} karaoke",
                download=False
            )
        return result.get("entries", [])
    
    def resolve(self, video_Id: str):
        with YoutubeDL(self.STREAM_OPTIONS) as ydl:
            result = ydl.extract_info(
                f"https://www.youtube.com/watch?v={video_Id}",
                download=False
            )
        formats = [f for f in result.get("formats", []) if (
            f.get("vcodec") != "none"
            and f.get("acodec") != "none"
            and f.get("url")
        )]

        if formats:
            best = formats[-1]
        else:
            best = result["formats"][-1]

        return {
            "videoId": video_Id,
            "title": result.get("title"),
            "duration": result.get("duration"),
            "thumbnail": result.get("thumbnail"),
            "streamUrl": best.get("url"),
            "format": {
                "id": best.get("format_id"),
                "ext": best.get("ext"),
                "resolution": best.get("resolution"),
                "fps": best.get("fps"),
                "vcodec": best.get("vcodec"),
                "acodec": best.get("acodec")
            }
        }
