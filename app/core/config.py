from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Karaoke Player"
    DEBUG: bool = False
    # REDIS_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()