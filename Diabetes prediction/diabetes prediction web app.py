# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 21:00:35 2026

@author: Shrinidhi
"""
#made this function as to take inputs from a user, and create a UI using streamlit. def diabetes_pred is for predicting the outcome of given data and in main we take the inputs
import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/Shrinidhi/OneDrive/Desktop/SY/projects/ML/Diabetes prediction/trained_model.sav', 'rb'))

    #creating function for prediction
def diabetes_prediction(input_data):
        
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
    
    
def main():
    
    #title
    st.title("diabetes prediction web app")
    #input data from user
    Pregnancies = st.text_input("number of pregnancies")
    Glucose = st.text_input("glucose level")
    BloodPressure = st.text_input("BP level")
    SkinThickness = st.text_input("skin thickness")
    Insulin = st.text_input("insulin level")
    BMI = st.text_input("BMI")
    DiabetesPedigreeFunction = st.text_input("diabetes pedigree function")
    Age = st.text_input("age")
    
    
    #code of prediction
    diagnosis = ''
    #button for prediction
    if st.button('Diabetes test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
    
if __name__=='__main__':

    main()

