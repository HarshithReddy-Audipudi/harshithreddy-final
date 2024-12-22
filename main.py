import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Initialize FastAPI app
app = FastAPI(
    title="Heart Disease Prediction API",
    description="API for predicting heart disease using an ML model",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Heart Disease Prediction API is running!"}

# Load the model
model_path = os.getenv("MODEL_PATH", "best_heart_model.pkl")
try:
    model = joblib.load(model_path)
except Exception as e:
    raise RuntimeError(f"Error loading the model: {str(e)}")

# Define Pydantic model for input validation
class PredictionRequest(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    thalach: int
    bmi_age_comb: float

@app.post("/predict/")
def predict(request: PredictionRequest):
    try:
        # Convert request data to a DataFrame
        input_data = pd.DataFrame([request.dict()])

        # Predict using the model
        prediction = model.predict(input_data)
        prediction_text = "Heart Disease" if prediction[0] == 1 else "No Heart Disease"

        return {"prediction": prediction_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
