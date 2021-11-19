from pydantic import BaseSettings

class Settings(BaseSettings):
    consumer_key: str = "3M3s8eZpwTyUxhIaEpsfwlO4w"
    consumer_secret: str = "D827LCm6B5fJ2DY4KvydOwDG7cdqeKqTSH8Ai9bQtMI6VN3vMs"
    access_token: str = "3164075700-UMmOwzGrPuzX5DkfUBZtXIg3f8DbcRlf77DnhvI"
    access_token_secret: str = "pOufkDfSvTANFmMputocPSMskeEYK7hIwYGdqVjTQR2xl"
    items_limit: int = 10

settings = Settings()