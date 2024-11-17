import streamlit as st

def calculate_bmi(weight, height):
    height_in_meters = height / 100  # Convert cm to meters
    bmi = weight / (height_in_meters ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Streamlit App
st.title("BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) and find out your ideal category.")

# Weight Input
weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)

# Height Input
height_unit = st.radio("Select Height Unit", ("Centimeters", "Feet and Inches"), horizontal=True)

if height_unit == "Centimeters":
    height = st.number_input("Height (cm)", min_value=0.0, step=0.1)
else:
    col1, col2 = st.columns(2)
    with col1:
        feet = st.number_input("Feet", min_value=0, step=1, format="%d")
    with col2:
        inches = st.number_input("Inches", min_value=0, max_value=11, step=1, format="%d")
    height = (feet * 12 + inches) * 2.54  # Convert feet and inches to cm
    st.write(f"Height in cm: {height:.2f} cm")

# Calculate BMI
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category = interpret_bmi(bmi)
        st.success(f"Your BMI is: {bmi:.2f}")
        st.info(f"Category: {category}")
    else:
        st.error("Please enter valid values for weight and height.")
