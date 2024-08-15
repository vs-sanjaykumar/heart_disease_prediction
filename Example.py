import os
import numpy as np
import pickle
import streamlit as st
import warnings 

#loading the saved Model
loaded_model=pickle.load(open('C:\learn front end\Heart-Disease-Prediction-with-clinical-variables-main\Heart-Disease-Prediction-with-clinical-variables-main\heart_disease_XGmodel.sav','rb'))


#creating a function for prediction
def heart_disease_prediction(input_data):

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
       return 'The Person does not have a Heart Disease'
    else:
       return 'The Person has Heart Disease'

def main():
   

   #give a title
    st.title('Heart Disease Prediction')
   
   #getting the input data from the user
    age=st.text_input('Age')

    sex=st.text_input('Sex')

    cp=st.text_input('Chest Pain Types')

    trestbps=st.text_input('Resting Blood Pressure')

    chol=st.text_input('Serum Cholestral in mg/dl')

    fbs=st.text_input('Fasting Blood Sugar > 120 mg/dl')

    restecg=st.text_input('Resting Electrocardiographic results')

    thalach=st.text_input('Maximum Heart Rate Achieved')

    exang=st.text_input('Exercise Induced Angina')

    oldpeak=st.text_input('ST depression induced by exercise')

    slope=st.text_input('Slope of the peak exercise ST segment')

    ca=st.text_input('Major vessels colored by flouroscopy')

    thal=st.text_input('thal: 0 = normal; 1= fixed defect; 2 = reversable defect')

    

    #code for prediction
    heart_diagnosis = ''

    #creating a button for prediction
    if st.button('Heart Disease Test Result'):
        heart_diagnosis = heart_disease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])

    st.success(heart_diagnosis)


if __name__=='__main__':
    main()