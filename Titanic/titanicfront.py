import requests
import streamlit as st


st.title('Titanic survival')

titanic_url = 'http://127.0.0.1:8000/titanic/predict'

Pclass = st.selectbox('Passenger class', [])