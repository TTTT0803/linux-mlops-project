from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI()

# Định nghĩa dữ liệu đầu vào (4 chỉ số của hoa Iris)
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Load model khi app khởi động
# Lưu ý: Chúng ta sẽ copy file model.pkl vào cùng thư mục này sau
model_path = "model.pkl"
model = None

if os.path.exists(model_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
else:
    print("CANH BAO: Khong tim thay file model.pkl!")

@app.get("/")
def home():
    return {"message": "MLOps API is running!"}

@app.post("/predict")
def predict(item: IrisInput):
    if not model:
        return {"error": "Model chua duoc load"}

    # Chuyen du lieu ve dang numpy array
    data = np.array([[item.sepal_length, item.sepal_width, item.petal_length, item.petal_width]])

    # Du doan
    prediction = model.predict(data)

    # Tra ve ket qua (0, 1, hoac 2)
    return {"prediction": int(prediction[0])}
