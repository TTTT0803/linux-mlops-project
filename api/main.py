from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI()

# 1. Định nghĩa dữ liệu đầu vào
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 2. Load model khi app khởi động
model_path = "model.pkl"
model = None

@app.on_event("startup")
def load_model():
    global model
    if os.path.exists(model_path):
        with open(model_path, "rb") as f:
            model = pickle.load(f)

# 3. API Dự đoán (Quan trọng)
@app.post("/predict")
def predict(data: IrisInput):
    if not model:
        return {"error": "Model not loaded"}
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(features)
    return {"prediction": str(prediction[0])}

# 4. API Trang chủ (ĐÂY LÀ CHỖ BẠN SỬA ĐỂ DEMO)
@app.get("/")
def root():
    # Sửa dòng dưới này thành câu bạn muốn hiển thị cho thầy xem
    return {"message": "DEMO FINAL: Chao Thay - He thong da tu dong update!"}
