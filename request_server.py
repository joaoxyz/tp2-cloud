import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import date

class Recommendation(BaseModel):
    playlist_ids: List[str]
    version: str
    model_date: str

class ModelInput(BaseModel):
    songs: List[str]

app = FastAPI()

with open('model_results.pickle', 'rb') as file:
    recommender = pickle.load(file)

@app.post("/api/recommend")
def generate_recommendation(inp : ModelInput) -> Recommendation:
    result = []
    for song in inp.songs:
        mask = [True if song in i else False for i in recommender['antecedents']]
        result += recommender[mask].explode('consequents')['consequents'].unique()
    result = list(set(result))
    return Recommendation(playlist_ids=result, version='1', model_date=date.today().isoformat())
