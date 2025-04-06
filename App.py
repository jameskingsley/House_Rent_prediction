#Import Dependecies
import numpy as np
import streamlit as st
import joblib


# Load the trained model
with open('House_Rent_model.pkl', 'rb') as f:
    model = joblib.load(f)

# Page config
st.set_page_config(page_title="Rent Prediction App", layout="centered")

#Styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        max-width: 700px;
        margin: auto;
        padding: 2rem;
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)
#App title
st.title("🏠 **House Rent Prediction**")

st.write("**Fill the form below to predict the estimated house rent.**")

#Inputs
size = st.number_input("Size (in sqft)", min_value=100,
    max_value=15000, step=50)

area_type = st.selectbox("Area Type", ['Carpet Area', 'Super Area'])
city = st.selectbox("City", ['Chennai', 'Delhi',
                    'Hyderabad', 'Kolkata', 'Mumbai'])
furnishing = st.selectbox("Furnishing Status", [
    'Semi-Furnished', 'Unfurnished', 'Furnished'])
tenant = st.selectbox("Tenant Preferred", [
    'Bachelors/Family', 'Family', 'Bachelors'])
contact = st.selectbox("Point of Contact", [
        'Contact Builder', 'Contact Owner', 'Contact Agent'])

#One-hot encoding manually
area_carpet = 1 if area_type == 'Carpet Area' else 0
area_super = 1 if area_type == 'Super Area' else 0

city_chennai = 1 if city == 'Chennai' else 0
city_delhi = 1 if city == 'Delhi' else 0
city_hyd = 1 if city == 'Hyderabad' else 0
city_kolkata = 1 if city == 'Kolkata' else 0
city_mumbai = 1 if city == 'Mumbai' else 0

furnish_semi = 1 if furnishing == 'Semi-Furnished' else 0
furnish_unfurnished = 1 if furnishing == 'Unfurnished' else 0

tenant_bachelors_family = 1 if tenant == 'Bachelors/Family' else 0
tenant_family = 1 if tenant == 'Family' else 0

contact_builder = 1 if contact == 'Contact Builder' else 0
contact_owner = 1 if contact == 'Contact Owner' else 0

# Feature array (excluding target 'Rent')
features = np.array([[
    size,
    area_carpet,
    area_super,
    city_chennai,
    city_delhi,
    city_hyd,
    city_kolkata,
    city_mumbai,
    furnish_semi,
    furnish_unfurnished,
    tenant_bachelors_family,
    tenant_family,
    contact_builder,
    contact_owner
]])

# Prediction
if st.button("Predict Rent "):
    rent_pred = model.predict(features)[0]
    st.success(f"Predicted Rent: ${rent_pred:,.2f}")





























































































