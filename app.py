
import streamlit as st
import joblib
import numpy as np

# Load the trained Random Forest model from the .pkl file
model = joblib.load('random_forest_model.pkl')

# Streamlit app title
st.title("Car Price Prediction App")

# Input fields for the user to enter car details
brand = st.selectbox("Select Car Brand", ['Toyota', 'BMW', 'Ford', 'Honda', 'Kia', 'Chevrolet'])
model_name = st.selectbox("Select Car Model", ['Corolla', 'Camry', 'X5', 'Mustang', 'Civic', 'Malibu'])
year = st.number_input("Enter Car Year", min_value=2000, max_value=2023, value=2020)
engine_size = st.number_input("Enter Engine Size (in L)", min_value=0.5, max_value=6.0, value=2.0)
fuel_type = st.selectbox("Select Fuel Type", ['Petrol', 'Diesel', 'Electric', 'Hybrid'])
transmission = st.selectbox("Select Transmission", ['Automatic', 'Manual'])
mileage = st.number_input("Enter Mileage (in km)", min_value=1000, max_value=500000, value=50000)
doors = st.number_input("Enter Number of Doors", min_value=2, max_value=5, value=4)
owner_count = st.number_input("Enter Number of Previous Owners", min_value=1, max_value=5, value=1)

# Prepare the input features for prediction (converting categorical variables to numeric)
brand_mapping = {'Toyota': 0, 'BMW': 1, 'Ford': 2, 'Honda': 3, 'Kia': 4, 'Chevrolet': 5}
model_mapping = {'Corolla': 0, 'Camry': 1, 'X5': 2, 'Mustang': 3, 'Civic': 4, 'Malibu': 5}
fuel_mapping = {'Petrol': 0, 'Diesel': 1, 'Electric': 2, 'Hybrid': 3}
transmission_mapping = {'Automatic': 0, 'Manual': 1}

# Convert the categorical inputs to numeric values
brand_encoded = brand_mapping.get(brand)
model_encoded = model_mapping.get(model_name)
fuel_encoded = fuel_mapping.get(fuel_type)
transmission_encoded = transmission_mapping.get(transmission)

# Prepare the input features as a numpy array
input_data = np.array([brand_encoded, model_encoded, year, engine_size, fuel_encoded, transmission_encoded, mileage, doors, owner_count])

# When the user clicks the "Predict" button
if st.button("Predict"):
    prediction = model.predict([input_data])
    st.write(f"Predicted Car Price: ${prediction[0]:,.2f}")

