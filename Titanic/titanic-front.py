import streamlit as st
import requests

st.title('Titanic Survival Check')

titanic_url = 'http://127.0.0.1:8000/titanic/predict'

# class TitanicSchema(BaseModel):
#     Pclass : int
#     Sex : str
#     Age : int
#     SibSp : int
#     Parch:int
#     Fare: float
#     Embarked: str

Pclass = st.selectbox('Person Class', [1,2,3])
Sex = st.selectbox('Gender',['male','female'])
Age = st.slider('Age', 0,120,18)
st.write("Passenger's Age is: ", Age)
SibSp = st.slider('Siblings', 0,15,0)
st.write(SibSp, ' siblings / spouses aboard the Titanic')
Parch = st.slider('Parents', 0,15,0)
st.write(Parch,' parents / children aboard the Titanic')
Fare = st.number_input('Fare', min_value=0, max_value=512, step=10)
Embarked = st.selectbox('Embarked', ['C', 'Q', 'S'])


passenger_data = {
    'Pclass' : Pclass,
    'Sex' : Sex,
    'Age' : Age,
    'SibSp' : SibSp,
    'Parch':Parch,
    'Fare': Fare,
    'Embarked': Embarked
}

if st.button('Predict'):
    try:
        response = requests.post(titanic_url, json=passenger_data,timeout=10)
        if response.status_code == 200:
            prediction = response.json()
            st.success(f"Answer: {prediction.get('Survived')}")
        else:
            st.error(f"Server response: {response.status_code}")
    except requests.exceptions.RequestException:
        st.error(f'Failed to connect to server!')

