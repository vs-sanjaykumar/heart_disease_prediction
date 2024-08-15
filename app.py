import os
import numpy as np
import pickle
import streamlit as st
import warnings

# Set Page Configuuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="👩🏻‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
heart_disease_model = pickle.load(open(r'C:\learn front end\Heart-Disease-Prediction-with-clinical-variables-main\Heart-Disease-Prediction-with-clinical-variables-main\heart_disease_XGmodel.sav', 'rb'))

# Heart Disease Prediction
st.title('Heart Disease Prediction using ML')
col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')

with col2:
    sex = st.text_input('Sex')

with col3:
    cp = st.text_input('Chest Pain Types')

with col1:
    trestbps = st.text_input('Resting Blood Pressure')

with col2:
    chol = st.text_input('Serum Cholestral in mg/dl')

with col3:
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

with col1:
    restecg = st.text_input('Resting Electrocardiographic results')

with col2:
    thalach = st.text_input('Maximum Heart Rate Achieved')

with col3:
    exang = st.text_input('Exercise Induced Angina')

with col1:
    oldpeak = st.text_input('ST depression induced by exercise')

with col2:
    slope = st.text_input('Slope of the peak exercise ST segment')

with col3:
    ca = st.text_input('Major vessels colored by flouroscopy')

with col1:
    thal = st.text_input('thal: 0 = normal; 1= fixed defect; 2 = reversable defect')

# code for prediction
heart_diagnosis = ''

# creating a button for prediction
if st.button('Heart Disease Test Result'):
    user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    user_input = [float(x) for x in user_input]
    heart_prediction = heart_disease_model.predict([user_input])

    if heart_prediction[0] == 1:
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'
st.success(heart_diagnosis)
