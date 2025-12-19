FROM python:3.10-slim
# Đổi tên biến này để ép Docker chạy lại từ đầu
# Đổi tên biến này để ép Docker KHÔNG ĐƯỢC DÙNG CACHE
ENV REFRESH_AT=2025_12_19_LAST_CHANCE
WORKDIR /app

# 1. Copy file cài đặt thư viện
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. QUAN TRỌNG: Copy file model vào
COPY vku_final.pkl .

# 3. Copy toàn bộ code còn lại
COPY . .

# 4. Chạy App
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# Force Rebuild Model
