import streamlit as st
import requests

st.title('Bank Credit Approval')

api_url = 'http://127.0.0.1:8000/credit/predict'

person_age = st.number_input("Client's age", min_value=18.0, max_value=80.0, step=1.0)
person_gender = st.selectbox('Gender', ['male', 'female'])
person_income = st.number_input('Annual income', min_value=0.0,step=100.0)
person_emp_exp = st.number_input('Employment experience', min_value=0,step=1)
loan_amnt = st.number_input('Loan amount', min_value=100.0, step=100.0)
loan_int_rate = st.number_input('Loan interest rate', min_value=0.0, step=1.0)
loan_percent_income = st.number_input('Loan percentage income', min_value=0.0, step=1.0)
cb_person_cred_hist_length = st.number_input('Client credit history length', min_value=0.0, step=1.0)
credit_score = st.number_input('Credit score', min_value=0, step=10)
previous_loan_defaults_on_file = st.selectbox('Previous loan defaults', ['Yes', 'No'])
person_education = st.selectbox('Education', ['Bachelor','Doctorate','High School', 'Master','Associate']) #БИР Вариант жок
person_home_ownership = st.selectbox('Home ownership', ['OTHER','OWN', 'RENT','MORTGAGE'])
loan_intent = st.selectbox('Credit intention', ['EDUCATION','HOMEIMPROVEMENT','MEDICAL','PERSONAL','VENTURE','DEBTCONSOLIDATION'])

client_data = {
    'person_age': person_age,
    'person_gender': person_gender,
    'person_income': person_income,
    'person_emp_exp': person_emp_exp,
    'loan_amnt': loan_amnt,
    'loan_int_rate': loan_int_rate,
    'loan_percent_income': loan_percent_income,
    'cb_person_cred_hist_length': cb_person_cred_hist_length,
    'credit_score': credit_score,
    'previous_loan_defaults_on_file': previous_loan_defaults_on_file,
    'person_education': person_education,
    'person_home_ownership': person_home_ownership,
    'loan_intent': loan_intent
}

if st.button('Check result'):
    try:
        answer = requests.post(api_url, json=client_data, timeout=10)
        if answer.status_code == 200:
            result = answer.json()
            st.success(f"Response: {result.get('Message')}")
        else:
            st.error(f'Server responded with {answer.status_code}')
    except requests.exceptions.RequestException:
        st.error(f'Failed to connect to server!')
