from fastapi import FastAPI

app = FastAPI()

@app.post("/api/recommend")
def read_root():
    return {"Hello": "World"}
