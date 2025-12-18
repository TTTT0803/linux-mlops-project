# 1. Chọn hệ điều hành nền (Python nhẹ)
FROM python:3.10-slim

# 2. Tạo thư mục làm việc bên trong container
WORKDIR /app

# 3. Copy file danh sách thư viện vào trước
COPY requirements.txt .

# 4. Cài đặt thư viện
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy toàn bộ code (main.py, model.pkl) vào container
COPY . .

# 6. Mở cổng 8000
EXPOSE 8000

# 7. Lệnh chạy server khi container khởi động
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
