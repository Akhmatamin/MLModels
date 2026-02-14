from fastapi import APIRouter
from pydantic import BaseModel
import joblib

scaler = joblib.load('Loan_Bank/scalerLoan.pkl')
model = joblib.load('Loan_Bank/modelLoan.pkl')

loan_long_rout = APIRouter(prefix='/loanpredict', tags=['LoanModel'])



class LoanData(BaseModel):
    person_age:float
    person_gender:str
    person_income:float
    person_emp_exp:int
    loan_amnt:float
    loan_int_rate:float
    loan_percent_income:float
    cb_person_cred_hist_length:float
    credit_score:int
    previous_loan_defaults_on_file:str
    person_education:str
    person_home_ownership:str
    loan_intent:str


education = ['Bachelor','Doctorate','High School', 'Master']
home = ['OTHER','OWN', 'RENT']
intent = ['EDUCATION','HOMEIMPROVEMENT','MEDICAL','PERSONAL','VENTURE']

@loan_long_rout.post('/predict')
async def predict(schema: LoanData):
    data = schema.dict()

    new_gender = data.pop('person_gender')
    gender0_1 = [1 if new_gender == 'male' else 0]

    new_loan_file = data.pop('previous_loan_defaults_on_file')
    loan_file0_1 = [1 if new_loan_file == 'Yes' else 0]

    new_education = data.pop('person_education')
    education0_1 = [1 if new_education == i else 0 for i in education]

    new_home = data.pop('person_home_ownership')
    home0_1 = [1 if new_home == i else 0 for i in home]

    new_intent = data.pop('loan_intent')
    intent0_1 = [1 if new_intent == i else 0 for i in intent]

    features = list(data.values()) + gender0_1 + loan_file0_1+ education0_1 + home0_1 + intent0_1
    scaled = scaler.transform([features])
    prediction = model.predict(scaled)
    prediction_w = 'Approved' if prediction == 1 else 'Rejected'
    print(prediction)
    return {'Message': prediction_w}



