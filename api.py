from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

class StudentData(BaseModel):
    cgpa: float
    aptitude_score: int
    communication_skill: int

@app.get("/")
def home():
    return {"message": "Placement Prediction API Running"}

@app.post("/predict")
def predict(data: StudentData):

    features = [[
        data.cgpa,
        data.aptitude_score,
        data.communication_skill
    ]]

    prediction = model.predict(features)[0]

    result = "Placed" if prediction == 1 else "Not Placed"

    return {
        "prediction": result
    }