import streamlit as st
import numpy as np
from src.mlProject.pipeline.prediction import PredictionPipeline
import os

# Title of the app
st.title("Wine Quality Prediction")

# Button to train the model
if st.button('Train Model'):
    os.system("python main.py")
    st.success("Training Successful!")

# Form for user input
with st.form(key='prediction_form'):
    fixed_acidity = st.number_input('Fixed Acidity', format="%.2f")
    volatile_acidity = st.number_input('Volatile Acidity', format="%.2f")
    citric_acid = st.number_input('Citric Acid', format="%.2f")
    residual_sugar = st.number_input('Residual Sugar', format="%.2f")
    chlorides = st.number_input('Chlorides', format="%.2f")
    free_sulfur_dioxide = st.number_input('Free Sulfur Dioxide', format="%.2f")
    total_sulfur_dioxide = st.number_input('Total Sulfur Dioxide', format="%.2f")
    density = st.number_input('Density', format="%.4f")
    pH = st.number_input('pH', format="%.2f")
    sulphates = st.number_input('Sulphates', format="%.2f")
    alcohol = st.number_input('Alcohol', format="%.2f")

    # Submit button
    submit_button = st.form_submit_button(label='Predict')

# Prediction logic
if submit_button:
    try:
        data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
        data = np.array(data).reshape(1, 11)

        obj = PredictionPipeline()
        predict = obj.predict(data)

        st.write(f"Prediction: {predict}")

    except Exception as e:
        st.error(f"An error occurred: {e}")