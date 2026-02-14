from fastapi import FastAPI
import uvicorn
from LoanBankShort.model import loan_router
from Diabetes.diabetes import diabetes_router
from Loan_Bank.loan import loan_long_rout
from Avocado.avocado import predict_router
from Titanic.titanic import titanic

app = FastAPI()
app.include_router(loan_router)
app.include_router(diabetes_router)

app.include_router(loan_long_rout)
app.include_router(predict_router)
app.include_router(titanic)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
