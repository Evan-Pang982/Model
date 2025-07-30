import joblib
import streamlit as st
import pandas as pd
import numpy as np
model = joblib.load('model_LC.pkl')
st.title('Lung Cancer Prediction App')

st.header("Patient Information")
age = st.number_input('Age', min_value=0, max_value=120, value=50)

gender_m = st.selectbox('Gender (M for Male, F for Female)', ['M', 'F'])
gender_m = 1 if gender_m == 'M' else 0

anxiety = st.selectbox('Do you experience anxiety?', ['No', 'Yes'])
anxiety = 1 if anxiety == 'Yes' else 0

peer_pressure = st.selectbox('Do you feel peer pressure?', ['No', 'Yes'])
peer_pressure = 1 if peer_pressure == 'Yes' else 0

swallowing_difficulty = st.selectbox('Do you have swallowing difficulty?', ['No', 'Yes'])
swallowing_difficulty = 1 if swallowing_difficulty == 'Yes' else 0

fatigue = st.selectbox('Do you feel fatigued?', ['No', 'Yes'])
fatigue = 1 if fatigue == 'Yes' else 0

chronic_disease = st.selectbox('Do you have any chronic disease?', ['No', 'Yes'])
chronic_disease = 1 if chronic_disease == 'Yes' else 0

alcohol_consuming = st.selectbox('Do you consume alcohol?', ['No', 'Yes'])
alcohol_consuming = 1 if alcohol_consuming == 'Yes' else 0

smoking = st.selectbox('Do you smoke?', ['No', 'Yes'])
smoking = 1 if smoking == 'Yes' else 0

allergy = st.selectbox('Do you have any allergies?', ['No', 'Yes'])
allergy = 1 if allergy == 'Yes' else 0

shortness_of_breath = st.selectbox('Do you have shortness of breath?', ['No', 'Yes'])
shortness_of_breath = 1 if shortness_of_breath == 'Yes' else 0

wheezing = st.selectbox('Do you experience wheezing?', ['No', 'Yes'])
wheezing = 1 if wheezing == 'Yes' else 0

yellow_fingers = st.selectbox('Do you have yellow fingers?', ['No', 'Yes'])
yellow_fingers = 1 if yellow_fingers == 'Yes' else 0

if st.button('Predict Lung Cancer Risk'):
    input_data = pd.DataFrame([{
        'AGE': age,
        'GENDER_M': gender_m,
        'ANXIETY_2': anxiety,
        'PEER_PRESSURE_2': peer_pressure,
        'SWALLOWING_DIFFICULTY_2': swallowing_difficulty,
        'FATIGUE_2': fatigue,
        'CHRONIC_DISEASE_2': chronic_disease,
        'ALCOHOL_CONSUMING_2': alcohol_consuming,
        'SMOKING_2': smoking,
        'ALLERGY_2': allergy,
        'SHORTNESS_OF_BREATH_2': shortness_of_breath,
        'WHEEZING_2': wheezing,
        'YELLOW_FINGERS_2': yellow_fingers
    }])
    expected_features = [
    'AGE', 'GENDER_M', 'ANXIETY_2', 'PEER_PRESSURE_2', 'SWALLOWING_DIFFICULTY_2',
    'FATIGUE_2', 'CHRONIC_DISEASE_2', 'ALCOHOL_CONSUMING_2', 'SMOKING_2',
    'ALLERGY_2', 'SHORTNESS_OF_BREATH_2', 'WHEEZING_2', 'YELLOW_FINGERS_2'
]

    input_data = input_data.reindex(columns=expected_features, fill_value=0)

    prediction = model.predict(input_data)[0]
    st.success(f'Lung Cancer?: ${prediction}$')
    
    # if prediction == 1:
    #     st.error('High risk of lung cancer detected.')
    # else:
    #     st.success('Low risk of lung cancer detected.')

st.markdown(f"""
            <style>
            .stApp{{
            background: url("https://tse4.mm.bing.net/th/id/OIP.pygl2RANrMju2yVHfromjAHaFI?rs=1&pid=ImgDetMain&o=7&rm=3")
            background-size: cover;
            }}
            </style>
            """, unsafe_allow_html=True)