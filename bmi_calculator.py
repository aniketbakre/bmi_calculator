import streamlit as st

def calculate_bmr(gender, weight, height, age):
    if gender == "Male":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "Female":
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

def convert_to_cm(feet, inches):
    total_inches = (feet * 12) + inches
    cm = total_inches * 2.54
    return cm

# Streamlit App
st.title("BMR Calculator")
st.write("Calculate your Basal Metabolic Rate (BMR)")

# Side-by-Side Radio Buttons for Gender and Height Unit
col1, col2 = st.columns(2)
with col1:
    gender = st.radio("Gender", ("Male", "Female"), horizontal=True)
with col2:
    height_unit = st.radio("Height Unit", ("Centimeters", "Feet and Inches"), horizontal=True)

# Weight Input
weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)

# Height Input
if height_unit == "Centimeters":
    height = st.number_input("Height (cm)", min_value=0.0, step=0.1)
else:
    # Input fields for feet and inches side by side
    col3, col4 = st.columns(2)
    with col3:
        feet = st.number_input("Feet", min_value=0, step=1, format="%d")
    with col4:
        inches = st.number_input("Inches", min_value=0, max_value=11, step=1, format="%d")
    # Convert feet and inches to cm
    height = convert_to_cm(feet, inches)
    st.write(f"Height in cm: {height:.2f} cm")

# Age Input
age = st.number_input("Age (years)", min_value=0, step=1)

# Calculate BMR
if st.button("Calculate BMR"):
    if weight > 0 and height > 0 and age > 0:
        bmr = calculate_bmr(gender, weight, height, age)
        st.success(f"Your BMR is: {bmr:.2f} kcal/day")
    else:
        st.error("Please enter valid values for weight, height, and age.")
