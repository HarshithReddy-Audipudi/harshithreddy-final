import os
import streamlit as st
import requests

# Determine the API URL
if os.getenv("DOCKER_ENV") == "true":  # Set this variable in your Docker container
    api_url = "http://host.docker.internal:8089/predict/"  # For Docker
else:
    api_url = "http://localhost:8089/predict/"  # For local testing

# Streamlit App
st.title("Heart Disease Prediction")

# Input Form
st.subheader("Enter the details below:")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", min_value=50, max_value=200)
chol = st.number_input("Cholesterol Level", min_value=100, max_value=600)
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250)
bmi_age_comb = age * trestbps

# Predict Button
if st.button("Predict"):
    data = {
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "thalach": thalach,
        "bmi_age_comb": bmi_age_comb,
    }
    try:
        response = requests.post(api_url, json=data)
        response.raise_for_status()  # Raise HTTPError for bad responses
        st.success(f"Prediction: {response.json()['prediction']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {str(e)}")
