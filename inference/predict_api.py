from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model.joblib")

# Initialize FastAPI app
app = FastAPI()

# Input schema
class InputData(BaseModel):
    duration: int
    amount: int
    age: int
    job: int
    housing: str
    purpose: str

@app.get("/")
def read_root():
    return {"message": "✅ Credit Risk Model API is running."}

@app.post("/predict")
def predict(data: InputData):
    input_df = pd.DataFrame([data.dict()])
    input_df_encoded = pd.get_dummies(input_df)

    # Make sure columns match the training set
    model_input_columns = model.feature_names_in_
    for col in model_input_columns:
        if col not in input_df_encoded:
            input_df_encoded[col] = 0
    input_df_encoded = input_df_encoded[model_input_columns]

    prediction = model.predict(input_df_encoded)
    return {"prediction": int(prediction[0])}
