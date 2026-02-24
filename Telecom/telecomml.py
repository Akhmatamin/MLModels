from fastapi import APIRouter
from pydantic import BaseModel
import joblib
from typing import Literal
import pandas as pd

scaler = joblib.load('Telecom/scalertl.pkl')
model = joblib.load('Telecom/tree_model.pkl')
training_columns = joblib.load('Telecom/columns.pkl')

telecom_router = APIRouter(prefix="/telecom", tags=["Telecom"])

class TelecomSchema(BaseModel):
    SeniorCitizen: int
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    gender: Literal["Female", "Male"]
    Partner: Literal["Yes", "No"]
    Dependents: Literal["Yes", "No"]
    PhoneService: Literal["Yes", "No"]
    MultipleLines: Literal["No phone service", "No", "Yes"]
    InternetService: Literal["DSL", "Fiber optic", "No"]
    OnlineSecurity: Literal["No", "Yes", "No internet service"]
    OnlineBackup: Literal["Yes", "No", "No internet service"]
    DeviceProtection: Literal["No", "Yes", "No internet service"]
    TechSupport: Literal["No", "Yes", "No internet service"]
    StreamingTV: Literal["No", "Yes", "No internet service"]
    StreamingMovies: Literal["No", "Yes", "No internet service"]
    Contract: Literal["Month-to-month", "One year", "Two year"]
    PaperlessBilling: Literal["Yes", "No"]
    PaymentMethod: Literal[
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]



def prepare_input(data: dict):
    df = pd.DataFrame([data])
    df = pd.get_dummies(df, columns=['gender','Partner','Dependents','PhoneService','MultipleLines','InternetService',
                                 'OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies',
                                 'Contract','PaperlessBilling','PaymentMethod'],drop_first=True)
    df = df.reindex(columns=training_columns, fill_value=0)
    return df

@telecom_router.post("/predict")
async def predict(schema: TelecomSchema):
    data = schema.dict()
    df = prepare_input(data)

    scaled = scaler.transform(df)
    prediction = model.predict(scaled)[0]
    # prediction = "Yes" if prediction == 1 else "No"

    return {"Churn": int(prediction)}



