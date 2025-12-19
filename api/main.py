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

# --- TÊN FILE MỚI ---
model_path = "vku_final.pkl"
model = None

@app.on_event("startup")
def load_model():
    global model
    # Debug xem file có thật không
    print(f"--- DEBUG: Checking for {model_path} ---")
    if os.path.exists(model_path):
        # Kiểm tra kích thước file
        size = os.path.getsize(model_path)
        print(f"File found! Size: {size} bytes")
        if size < 1000: # Nếu nhỏ hơn 1KB là file lỗi
             print("❌ ERROR: File too small (Corrupted)!")
        else:
            with open(model_path, "rb") as f:
                model = pickle.load(f)
            print("✅ SUCCESS: Model loaded!")
    else:
        print(f"❌ ERROR: File {model_path} not found!")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(data: StudentInput):
    if not model:
        return {"error": "Model not loaded. Check server logs."}
    
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
