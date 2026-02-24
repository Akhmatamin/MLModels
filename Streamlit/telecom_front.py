import streamlit as st
import requests

st.title('Telecom Churn Prediction')

telecom_url = 'http://127.0.0.1:8000/telecom/predict'

SeniorCitizen = st.selectbox('Senior Citizen', [0, 1])
tenure = st.slider('Tenure (months)', 0, 72, 12)
MonthlyCharges = st.number_input('Monthly Charges', min_value=0.0, step=10.0)
TotalCharges = st.number_input('Total Charges', min_value=0.0, step=50.0)
gender = st.selectbox('Gender', ['Female', 'Male'])
Partner = st.selectbox('Partner', ['Yes', 'No'])
Dependents = st.selectbox('Dependents', ['Yes', 'No'])
PhoneService = st.selectbox('Phone Service', ['Yes', 'No'])
MultipleLines = st.selectbox(
    'Multiple Lines',
    ['No phone service', 'No', 'Yes']
)
InternetService = st.selectbox(
    'Internet Service',
    ['DSL', 'Fiber optic', 'No']
)
OnlineSecurity = st.selectbox(
    'Online Security',
    ['No', 'Yes', 'No internet service']
)
OnlineBackup = st.selectbox(
    'Online Backup',
    ['No', 'Yes', 'No internet service']
)

DeviceProtection = st.selectbox(
    'Device Protection',
    ['No', 'Yes', 'No internet service']
)

TechSupport = st.selectbox(
    'Tech Support',
    ['No', 'Yes', 'No internet service']
)

StreamingTV = st.selectbox(
    'Streaming TV',
    ['No', 'Yes', 'No internet service']
)

StreamingMovies = st.selectbox(
    'Streaming Movies',
    ['No', 'Yes', 'No internet service']
)

Contract = st.selectbox(
    'Contract',
    ['Month-to-month', 'One year', 'Two year']
)

PaperlessBilling = st.selectbox('Paperless Billing', ['Yes', 'No'])

PaymentMethod = st.selectbox(
    'Payment Method',
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

telecom_data = {
    "SeniorCitizen": SeniorCitizen,
    "tenure": tenure,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges,
    "gender": gender,
    "Partner": Partner,
    "Dependents": Dependents,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod
}

if st.button('Predict'):
    try:
        response = requests.post(telecom_url, json=telecom_data,timeout=10)
        if response.status_code == 200:
            prediction = response.json()
            st.success(f"Answer: {prediction.get('Churn')}")
        else:
            st.error(f"Server response: {response.status_code}")
    except requests.exceptions.RequestException:
        st.error(f'Failed to connect to server!')