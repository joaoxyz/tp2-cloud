import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import date

class Recommendation(BaseModel):
    playlist_ids: List[str]
    version: int
    model_date: str

class ModelInput(BaseModel):
    songs: List[str]

app = FastAPI()

with open('/home/joaomiranda/project2-pv/model_results.pickle', 'rb') as file:
    recommender = pickle.load(file)

@app.post("/api/recommend")
async def generate_recommendation(inp : ModelInput) -> Recommendation:
    result = []
    for song in inp.songs:
        step1 = recommender[[True if song in i else False for i in recommender['antecedents']]]
        step2 = step1.explode('consequents')
        result += step2['consequents'].unique().tolist()
    result = list(set(result))
    return Recommendation(playlist_ids=result, version=1, model_date=date.today().isoformat())
