import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("best_model.joblib")
scaler = joblib.load("scaler.joblib")

st.title("Dry Bean Classification")

features = []

feature_names = [
    'Area',
    'Perimeter',
    'MajorAxisLength',
    'MinorAxisLength',
    'AspectRation',
    'Eccentricity',
    'ConvexArea',
    'EquivDiameter',
    'Extent',
    'Solidity',
    'roundness',
    'Compactness',
    'ShapeFactor1',
    'ShapeFactor2',
    'ShapeFactor3',
    'ShapeFactor4'
]

for feature in feature_names:
    value = st.number_input(feature)
    features.append(value)

if st.button("Predict"):

    data = np.array(features).reshape(1, -1)

    data = scaler.transform(data)

    prediction = model.predict(data)

    st.success(f"Bean Type: {prediction[0]}")