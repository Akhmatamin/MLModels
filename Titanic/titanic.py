from fastapi import APIRouter
from pydantic import BaseModel
import joblib

titanic = APIRouter(prefix="/titanic", tags=["Titanic"])

model = joblib.load("Titanic/titanic_model.pkl")
scaler = joblib.load("Titanic/titanic_scaler.pkl")

class TitanicSchema(BaseModel):
    Pclass : int
    Sex : str
    Age : int
    SibSp : int
    Parch:int
    Fare: float
    Embarked: str

@titanic.post("/")
async def predict(schema: TitanicSchema):
    data = schema.dict()

    embarked = data.pop("Embarked")
    embarked0_1 = [
        1 if embarked == "S" else 0,
        1 if embarked == "Q" else 0,
    ]

    gender = data.pop("Sex")
    gender0_1 = [
        1 if gender == "female" else 0,
    ]

    features = list(data.values()) + embarked0_1 + gender0_1
    scaled = scaler.transform([features])
    prediction = int(model.predict(scaled)[0])
    return {'Survived': 'Alive' if prediction == 1 else 'Dead'}