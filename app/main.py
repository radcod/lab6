from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/predict")
def predict(value: float):
    prediction = model.predict(np.array([[value]]))[0]

    return {
        "name": "YOUR_NAME",
        "roll_no": "YOUR_ROLL_NO",
        "wine_quality": int(prediction)
    }