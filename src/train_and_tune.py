import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv("data/staged/data.csv")

# Separate features and target
X = df.drop("class", axis=1)
y = df["class"]

# Encode categorical variables
X_encoded = pd.get_dummies(X)

# Encode target if it's string (like 'good'/'bad')
if y.dtype == object:
    y = y.astype('category').cat.codes

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.joblib")
print("✅ Model trained and saved to model.joblib")
