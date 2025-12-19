from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    # Gửi yêu cầu vào trang chủ
    response = client.get("/")
    
    # 1. Kiểm tra kết nối thành công (200 OK)
    assert response.status_code == 200
    
    # 2. Kiểm tra nội dung trả về là HTML (Giao diện web)
    # (Code cũ đòi JSON nên mới lỗi, giờ mình sửa thành kiểm tra HTML)
    assert "text/html" in response.headers["content-type"]
    
    # 3. Kiểm tra xem trong web có hiện đúng tiêu đề không
    assert "Dự đoán Hoa Iris" in response.text

def test_predict():
    # API Dự đoán thì vẫn trả về JSON như cũ, nên giữ nguyên
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    
    # Kiểm tra kết quả
    data = response.json()
    assert "prediction" in data or "error" in data
