from fastapi import FastAPI
from typing import Optional
import uvicorn
from pydantic import BaseModel
from sklearn.ensemble import RandomForestClassifier
import pickle

app = FastAPI()

class Data_for_model(BaseModel):
    city_development_index: float
    gender: float
    relevent_experience: float
    enrolled_university: float
    experience: float
    company_size: float
    company_type: float
    last_new_job: float
    training_hours: float
    Graduate: float
    High_School: float
    Masters: float
    Phd: float
    Primary_School: float
    Arts: float
    Business_Degree: float
    Humanities: float
    No_Major: float
    Other: float
    STEM: float

@app.post("/predict/")
async def read_item(data: Data_for_model):

    X = [list(dict(data).values())]

    with open('project_model.pickl', 'rb') as f:
        model = pickle.load(f)

    pred = model.predict_proba(X)[0]
    return {0: pred[0], 1:pred[1]}

@app.get("/")
async def root():
    return {"message": "Hello"}

if __name__ == "__main__":
    uvicorn.run('implemet_model:app',reload=True)
