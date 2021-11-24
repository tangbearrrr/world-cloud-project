from pydantic import BaseSettings

class Settings(BaseSettings):
    consumer_key: str = ""
    consumer_secret: str = ""
    access_token: str = ""
    access_token_secret: str = ""
    items_limit: int = 100
    system_dir: str = "/Users/pattaweechitnapovn/Desktop/"

settings = Settings()