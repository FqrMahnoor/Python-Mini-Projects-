# Importing the Streamlit library
import streamlit as st   

# Setting the page title, icon, and layout
st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="centered")

# Displaying the app title
st.title("Unit Converter App")

# Dropdown menu to select the category of conversion
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Based on selected category, show relevant conversion options
if category == "Length":
    unit = st.selectbox("Select Conversion", [
        "Meters to Kilometers", "Kilometers to Meters",
        "Kilometers to Miles", "Miles to Kilometers"
    ])
elif category == "Time":
    unit = st.selectbox("Select Conversion", [
        "Seconds to Minutes", "Seconds to Hour",
        "Minutes to Seconds", "Minutes to Hours",
        "Hours to Seconds", "Hours to Minutes"
    ])
elif category == "Weight":
    unit = st.selectbox("Select Conversion", [
        "Kilograms to Pounds", "Pounds to Kilograms"
    ])

# Input field for user to enter the value they want to convert
value = st.number_input("Enter the value to convert")

# Function that handles all the conversions
def unit_converter(category, unit, value):
    if category == "Length":
        if unit == "Kilometers to Meters":
            return value * 1000
        elif unit == "Meters to Kilometers":
            return value / 1000
        elif unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Seconds to Hour":
            return value / 3600
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Seconds":
            return value * 3600
        elif unit == "Hours to Minutes":
            return value * 60

# Button that triggers the conversion when clicked
if st.button("Convert"):
    result = unit_converter(category, unit, value)  # Call the conversion function
    st.success(f"The result is {result:.2f}")  # Show the result rounded to 2 decimal places

    # Show the formula used if a value was entered
    if value != 0:
        if category == "Length":
            if unit == "Kilometers to Meters":
                st.info("📐 Formula: 1 Kilometer = 1000 Meters")
            elif unit == "Meters to Kilometers":
                st.info("📐 Formula: 1 Meter = 0.001 Kilometers")
            elif unit == "Kilometers to Miles":
                st.info("📐 Formula: 1 Kilometer = 0.621371 Miles")
            elif unit == "Miles to Kilometers":
                st.info("📐 Formula: 1 Mile = 1.60934 Kilometers")
        elif category == "Weight":
            if unit == "Kilograms to Pounds":
                st.info("📐 Formula: 1 Kilogram = 2.20462 Pounds")
            elif unit == "Pounds to Kilograms":
                st.info("📐 Formula: 1 Pound = 0.453592 Kilograms")
        elif category == "Time":
            if unit == "Seconds to Minutes":
                st.info("📐 Formula: 1 Minute = 60 Seconds")
            elif unit == "Seconds to Hour":
                st.info("📐 Formula: 1 Hour = 3600 Seconds")
            elif unit == "Minutes to Seconds":
                st.info("📐 Formula: 1 Minute = 60 Seconds")
            elif unit == "Minutes to Hours":
                st.info("📐 Formula: 1 Hour = 60 Minutes")
            elif unit == "Hours to Seconds":
                st.info("📐 Formula: 1 Hour = 3600 Seconds")
            elif unit == "Hours to Minutes":
                st.info("📐 Formula: 1 Hour = 60 Minutes")
