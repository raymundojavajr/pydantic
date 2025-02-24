from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import numpy as np

app = FastAPI()

# Load the trained ML model and feature names
model = joblib.load("house_price_model.pkl")
feature_names = joblib.load("model_features.pkl")


class HouseFeatures(BaseModel):
    square_feet: int = Field(..., gt=300, lt=10000, description="Size of house in square feet")
    bedrooms: int = Field(..., ge=1, le=10, description="Number of bedrooms")
    bathrooms: int = Field(..., ge=1, le=5, description="Number of bathrooms")
    location: str = Field(..., pattern="^(urban|suburban|rural)$", description="House location type")

@app.post("/predict/")
def predict_price(features: HouseFeatures):
    # Convert input into model-compatible format
    input_data = np.array([
        features.square_feet,
        features.bedrooms,
        features.bathrooms,
        1 if features.location == "suburban" else 0,  # Convert categorical
        1 if features.location == "rural" else 0
    ]).reshape(1, -1)

    # Predict house price
    predicted_price = model.predict(input_data)[0]

    return {"predicted_price": round(predicted_price, 2)}


@app.get("/")
def home():
    return {"message": "House Price Prediction API with FastAPI & Pydantic!"}
