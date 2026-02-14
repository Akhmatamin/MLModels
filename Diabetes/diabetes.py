from fastapi import APIRouter
from pydantic import BaseModel
import joblib
from scipy.constants import astronomical_unit

model = joblib.load('Diabetes/diabetes_model.pkl')
scaler = joblib.load('Diabetes/diabetes_scaler.pkl')


diabetes_router = APIRouter(prefix="/diabetes", tags=["diabetes"])

class DiabetesPrediction(BaseModel):
    Pregnancies: int
    Glucose : float
    BloodPressure: float
    BMI: int
    DiabetesPedigreeFunction: float
    Age: int

@diabetes_router.post("/predict")
async def predict_diabetes(schema: DiabetesPrediction):
    data = schema.dict()

    features = list(data.values())
    scaled = scaler.transform([features])
    prediction = model.predict(scaled)[0]
    prediction = int(prediction)
    prediction = 'No diabetes' if prediction == 0 else 'Yes,Diabetes'
    return {'Diabetes_outcome': prediction}