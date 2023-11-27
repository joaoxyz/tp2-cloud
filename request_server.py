from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Response(BaseModel):
    playlist_ids: List[str]
    version: str
    model_date: str

@app.post("/api/recommend")
def generate_recommendation(resp : Response):
    pass
