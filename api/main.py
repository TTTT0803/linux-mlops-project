from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI()

# Cấu hình để load giao diện từ thư mục templates
templates = Jinja2Templates(directory="templates")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Load Model
model_path = "model.pkl"
model = None

@app.on_event("startup")
def load_model():
    global model
    if os.path.exists(model_path):
        with open(model_path, "rb") as f:
            model = pickle.load(f)

# API hiển thị giao diện đẹp (Home Page)
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API Dự đoán (Backend xử lý)
@app.post("/predict")
def predict(data: IrisInput):
    if not model:
        return {"error": "Model not loaded"}
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(features)
    return {"prediction": str(prediction[0])}
