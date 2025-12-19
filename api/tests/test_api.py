from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    # 1. Kiểm tra trang chủ có hoạt động không
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    
    # 2. Kiểm tra xem giao diện có hiện chữ "VKU" không
    # (Lúc nãy lỗi do nó đi tìm chữ "Hoa Iris" mà không thấy)
    assert "VKU" in response.text

def test_predict():
    # 3. Gửi điểm thi giả lập (Toán, Lý, Anh)
    # (Lúc nãy lỗi do gửi nhầm kích thước hoa)
    payload = {
        "toan": 9.0,
        "ly": 8.5,
        "anh": 7.5
    }
    
    response = client.post("/predict", json=payload)
    
    # 4. Kiểm tra kết quả trả về
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    # Kiểm tra xem máy có khen câu nào không
    assert "chúc mừng" in data["prediction"].lower() or "tiếc" in data["prediction"].lower() or "xuất sắc" in data["prediction"].lower()

