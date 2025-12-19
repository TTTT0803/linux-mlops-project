from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class StudentInput(BaseModel):
    toan: float
    ly: float
    anh: float

model_path = "vku_model.pkl"
model = None

@app.on_event("startup")
def load_model():
    global model
    if os.path.exists(model_path):
        with open(model_path, "rb") as f:
            model = pickle.load(f)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(data: StudentInput):
    if not model:
        return {"error": "Model not loaded"}
    features = np.array([[data.toan, data.ly, data.anh]])
    prediction = model.predict(features)[0]
    
    ket_qua = ""
    if prediction == 0:
        ket_qua = "😢 Rất tiếc, chưa đủ điểm."
    elif prediction == 1:
        ket_qua = "🚢 Chúc mừng! Đậu ngành Logistics."
    else:
        ket_qua = "💻 Xuất sắc! Đậu ngành CNTT (Global)."
        
    return {"prediction": ket_qua}
# Force update model
