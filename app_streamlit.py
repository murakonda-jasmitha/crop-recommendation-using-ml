import streamlit as st
import joblib
import pandas as pd

bundle = joblib.load("crop_recommendation_model.pkl")


pipeline = bundle["pipeline"]
label_encoder = bundle["label_encoder"]
feature_columns = bundle["feature_columns"]

st.title("🌾 Crop Recommendation System")
st.write("Enter the soil and weather conditions to get the best crop recommendation.")

# Input widgets
inputs = {}
for col in feature_columns:
    inputs[col] = st.number_input(
        f"Enter {col}:", 
        value=0.0, 
        format="%.4f"
    )

# Predict Button
if st.button("Predict Crop"):
    df = pd.DataFrame([inputs.values()], columns=feature_columns)
    pred = pipeline.predict(df)[0]
    crop_name = label_encoder.inverse_transform([pred])[0]
    
    st.success(f"🌱 Recommended Crop: **{crop_name}**")
