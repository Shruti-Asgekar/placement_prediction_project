import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import mlflow
import mlflow.sklearn

# Load dataset
data = pd.read_csv("student_data.csv")

X = data[["cgpa", "aptitude_score", "communication_skill"]]
y = data["placed"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Start MLFlow
mlflow.set_experiment("Placement Prediction")

with mlflow.start_run():
    model = LogisticRegression()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    mlflow.log_param("model", "LogisticRegression")
    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(model, "placement-model")

    joblib.dump(model, "model.pkl")

    print("Model trained successfully")
    print("Accuracy:", accuracy)