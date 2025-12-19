import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np

# 1. Tạo dữ liệu giả lập (Học sinh thi vào VKU)
# Toán, Lý, Anh
# Output: 0 (Trượt), 1 (Logistics), 2 (CNTT)
data = {
    'toan': [8.5, 9.0, 5.0, 6.5, 7.0, 9.5, 4.0, 8.0, 7.5, 5.5],
    'ly':   [8.0, 9.0, 5.5, 6.0, 7.5, 9.5, 4.5, 7.5, 8.0, 5.0],
    'anh':  [7.5, 8.5, 4.0, 6.0, 7.0, 9.0, 3.5, 8.5, 7.0, 4.5],
    'ket_qua': [1, 2, 0, 0, 1, 2, 0, 2, 1, 0]
}

df = pd.DataFrame(data)
X = df[['toan', 'ly', 'anh']]
y = df['ket_qua']

# 2. Huấn luyện Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 3. Lưu Model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Đã train xong Model tuyển sinh VKU!")
