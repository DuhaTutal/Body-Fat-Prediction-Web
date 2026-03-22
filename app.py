import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory = "templates")


with open("body_fat_model.pkl", "rb") as f:
    saved_data = pickle.load(f)
    model = saved_data["model"]
    scaler = saved_data['scaler']


class Features(BaseModel):
    Age : int
    Weight : float
    Neck: float
    Chest: float
    Abdomen: float
    Hip: float
    Thigh: float
    Knee: float
    Ankle: float
    Biceps: float
    Forearm: float
    Wrist: float

@app.get("/",response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(features: Features):
    input_data = pd.DataFrame([features.model_dump()])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    return {"predicted_body_fat" : float(prediction)}
