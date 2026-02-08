from fastapi import FastAPI
import uvicorn
from model import loan_router
from diabetes import diabetes_router

app = FastAPI()
app.include_router(loan_router)
app.include_router(diabetes_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
