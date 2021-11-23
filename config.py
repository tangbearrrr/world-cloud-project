from pydantic import BaseSettings

class Settings(BaseSettings):
    consumer_key: str = ""
    consumer_secret: str = ""
    access_token: str = ""
    access_token_secret: str = ""
    items_limit: int = 100
    image_dir: str = "/Users/rahatsarawasee/Desktop/covid.png"

settings = Settings()