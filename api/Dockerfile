FROM python:3.9-slim
WORKDIR /app

# 1. Copy file cài đặt thư viện
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. QUAN TRỌNG: Copy file model vào
COPY model.pkl .

# 3. Copy toàn bộ code còn lại
COPY . .

# 4. Chạy App
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
