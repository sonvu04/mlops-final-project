import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load the dataset
df = pd.read_csv("data/staged/data.csv")

# Separate features and target
X = df.drop("class", axis=1)
y = df["class"]

# Encode categorical features
X_encoded = pd.get_dummies(X)

# Encode target labels if they are strings
if y.dtype == object:
    y = y.astype("category").cat.codes

# Split the data (same seed as training for reproducibility)
_, X_test, _, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Load the trained model
model = joblib.load("model.joblib")

# Predict
y_pred = model.predict(X_test)

# Save the evaluation report to a file with UTF-8 encoding
with open("evaluation.txt", "w", encoding="utf-8") as f:
    f.write("📊 Classification Report:\n")
    f.write(classification_report(y_test, y_pred))

print("✅ Evaluation saved to evaluation.txt")
