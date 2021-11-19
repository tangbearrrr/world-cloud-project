from typing import Optional
from fastapi import FastAPI
from tweepy_service import search

app = FastAPI()

@app.get("/api/v1/world-clouds")
def read_root():
    return search()