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

# Tên file model chuẩn
model_path = "model_final.pkl"
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
    # Kiểm tra model đã load chưa
    if not model:
        return {"error": "Model not loaded"}
    
    # Dự đoán
    features = np.array([[data.toan, data.ly, data.anh]])
    prediction = model.predict(features)[0]
    
    # Chuyển kết quả thành chữ
    ket_qua = ""
    if prediction == 0:
        ket_qua = "😢 Rất tiếc, chưa đủ điểm."
    elif prediction == 1:
        ket_qua = "🚢 Chúc mừng! Đậu ngành Logistics."
    else:
        ket_qua = "💻 Xuất sắc! Đậu ngành CNTT (Global)."
        
    return {"prediction": ket_qua}
