import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# KET NOI TOI MLFLOW (Vi chay tren cung may nen dung localhost)
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("Do_An_MLOps_Nhom_Minh")

# Load Data
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# Train & Log
print("Bat dau train model...")
with mlflow.start_run():
    n_estimators = 50
    clf = RandomForestClassifier(n_estimators=n_estimators)
    clf.fit(X_train, y_train)

    # Predict
    predictions = clf.predict(X_test)
    acc = accuracy_score(y_test, predictions)

    # Log len MLflow
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(clf, "model")

    print(f"Train xong! Do chinh xac: {acc}")
