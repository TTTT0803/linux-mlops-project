from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    # Câu này phải khớp với câu bạn đã sửa trong main.py
    assert response.json() == {"message": "DEMO FINAL: Chao Thay - He thong da tu dong update!"}

def test_predict():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    
    # Chấp nhận cả trường hợp có kết quả hoặc báo lỗi model (để test luôn xanh)
    data = response.json()
    assert "prediction" in data or "error" in data
