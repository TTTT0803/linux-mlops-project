from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data va train nhanh
iris = load_iris()
clf = RandomForestClassifier(n_estimators=50)
clf.fit(iris.data, iris.target)

# Luu thanh file model.pkl
with open("model.pkl", "wb") as f:
    pickle.dump(clf, f)

print("Da tao file model.pkl thanh cong!")
