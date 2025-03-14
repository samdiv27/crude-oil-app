import streamlit as st
import pandas as pd
import joblib

# Load models
api_model = joblib.load("api_model.pkl")
viscosity_model = joblib.load("viscosity_model.pkl")
sulfur_model = joblib.load("sulfur_model.pkl")
failure_model = joblib.load("failure_model.pkl")

# App title
st.title("Crude Oil & Well Monitoring App")

# User input
st.sidebar.header("Input Features")
water_cut = st.sidebar.slider("Water Cut (%)", 0.0, 50.0, 25.0)
pressure = st.sidebar.slider("Pressure (psi)", 100.0, 500.0, 300.0)
temperature = st.sidebar.slider("Temperature (°C)", 50.0, 150.0, 100.0)
gas_migration = st.sidebar.slider("Gas Migration (m/s)", 0.0, 10.0, 5.0)
vibration = st.sidebar.slider("Vibration (mm/s)", 0.0, 5.0, 2.5)

# Create input DataFrame
input_data = pd.DataFrame({
    'Water_Cut': [water_cut],
    'Pressure': [pressure],
    'Temperature': [temperature],
    'Gas_Migration': [gas_migration],
    'Vibration': [vibration]
})

# Display input
st.subheader("Your Input")
st.write(input_data)

# Predict
if st.button("Predict"):
    api_pred = api_model.predict(input_data)[0]
    visc_pred = viscosity_model.predict(input_data)[0]
    sulfur_pred = sulfur_model.predict(input_data)[0]
    failure_pred = failure_model.predict(input_data)[0]

    st.subheader("Predictions")
    st.write(f"API Gravity: {api_pred:.2f}")
    st.write(f"Viscosity: {visc_pred:.2f} cP")
    st.write(f"Sulfur Content: {sulfur_pred:.2f}%")
    st.write(f"Well Failure: {'Yes' if failure_pred == 1 else 'No'}")