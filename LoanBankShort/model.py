from fastapi import APIRouter
from pydantic import BaseModel
import joblib


scaler = joblib.load('LoanBankShort/scaler_short_loan.pkl')
model = joblib.load('LoanBankShort/model_log_short.pkl')

loan_router = APIRouter(prefix="/loan", tags=["Loan Approval"])


class LoanPredictSchema(BaseModel):
    person_age:int
    person_income: int
    person_emp_exp : int
    loan_amnt: int
    loan_int_rate : int
    credit_score : int
    person_home_ownership: str

ownership = ['RENT','OWN','OTHER']

@loan_router.post("/predict")
async def predict(schema: LoanPredictSchema):
    data = schema.dict()

    new_data = data.pop('person_home_ownership')
    home0_1 = [1 if new_data == i else 0 for i in ownership]

    features = list(data.values()) + home0_1
    scaled = scaler.transform([features])
    prediction = model.predict(scaled)[0]
    prediction = int(prediction)
    prediction = 'Rejected' if prediction == 0 else 'Approved'
    return {'loan_status': prediction}

