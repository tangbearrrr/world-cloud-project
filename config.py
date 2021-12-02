from pydantic import BaseSettings

class Settings(BaseSettings):
    consumer_key: str = "" #Enter your consumer key
    consumer_secret: str = "" #Enter your consumer key secret
    access_token: str = "" #Enter your access token
    access_token_secret: str = "" #Enter your access token secret
    items_limit: int = 100 
    system_dir: str = "front-end/public/" 

settings = Settings()