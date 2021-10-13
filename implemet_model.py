from fastapi import FastAPI
from typing import Optional
import uvicorn
from pydantic import BaseModel
from sklearn.ensemble import RandomForestClassifier
import pickle

app = FastAPI()

class Item (BaseModel):
    name: str
    number: int
    opt: Optional[str] = None

@app.post("/item/")
async def read_item(item: Item):
    return '0'

@app.get("/")
async def root():
    with open('model.pickl', 'rb') as f:
        model = pickle.load(f)


    return {"message": " ".join([str(i) for i in model.classes_])}

if __name__ == "__main__":
    uvicorn.run('main:app',reload=True)
