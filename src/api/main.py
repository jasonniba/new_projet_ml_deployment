from fastapi import FastAPI
from pydantic import BaseModel
from src.model import predict_model

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: InputData):
    result = predict_model(data.feature1, data.feature2)
    return {"prediction": result}