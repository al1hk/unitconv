import streamlit as st
import time

# Custom styling for a modern look
st.markdown("""
    <style>
        body {
            background-color: #0d1117;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            background-color: #0d1117;
        }
        .title {
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
            color: #58a6ff;
            margin-bottom: 1rem;
        }
        .convert-btn {
            background-color: #58a6ff;
            color: white;
            font-size: 1.2rem;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px;
            border: none;
            width: 100%;
        }
        .convert-btn:hover {
            background-color: #1f6feb;
        }
        .result-box {
            background-color: #161b22;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            margin-top: 10px;
        }
        .footer {
            text-align: center;
            font-size: 1rem;
            margin-top: 20px;
            color: #8b949e;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🔄 Google-Style Unit Converter</p>', unsafe_allow_html=True)

# Unit categories
categories = {
    "Length": ["meters", "kilometers", "centimeters", "miles", "feet", "inches"],
    "Mass": ["kilograms", "grams", "pounds", "ounces", "tons"],
    "Force": ["newtons", "dynes", "pounds-force", "kilograms-force"]
}

# Select category
category = st.selectbox("Select Unit Category", list(categories.keys()))

# Get units based on selected category
units = categories[category]

# Input fields
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# Dropdown selections for units
col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("From", units)

with col2:
    to_unit = st.selectbox("To", units)

# Conversion logic
def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {
            "meters": {"kilometers": value / 1000, "centimeters": value * 100, "miles": value * 0.000621371, "feet": value * 3.28084, "inches": value * 39.3701},
            "kilometers": {"meters": value * 1000, "centimeters": value * 100000, "miles": value * 0.621371, "feet": value * 3280.84, "inches": value * 39370.1},
            "centimeters": {"meters": value / 100, "kilometers": value / 100000, "miles": value * 0.0000062137, "feet": value * 0.0328084, "inches": value * 0.393701},
            "miles": {"meters": value / 0.000621371, "kilometers": value / 0.621371, "centimeters": value / 0.0000062137, "feet": value * 5280, "inches": value * 63360},
            "feet": {"meters": value * 0.3048, "kilometers": value * 0.0003048, "centimeters": value * 30.48, "miles": value * 0.000189394, "inches": value * 12},
            "inches": {"meters": value * 0.0254, "kilometers": value * 0.0000254, "centimeters": value * 2.54, "miles": value * 0.0000157828, "feet": value / 12},
        },
        "Mass": {
            "kilograms": {"grams": value * 1000, "pounds": value * 2.20462, "ounces": value * 35.274, "tons": value * 0.00110231},
            "grams": {"kilograms": value / 1000, "pounds": value * 0.00220462, "ounces": value * 0.035274, "tons": value * 0.00000110231},
            "pounds": {"kilograms": value * 0.453592, "grams": value * 453.592, "ounces": value * 16, "tons": value * 0.0005},
            "ounces": {"kilograms": value * 0.0283495, "grams": value * 28.3495, "pounds": value * 0.0625, "tons": value * 0.00003125},
            "tons": {"kilograms": value * 907.185, "grams": value * 907184.74, "pounds": value * 2000, "ounces": value * 32000},
        },
        "Force": {
            "newtons": {"dynes": value * 100000, "pounds-force": value * 0.224809, "kilograms-force": value * 0.101972},
            "dynes": {"newtons": value * 0.00001, "pounds-force": value * 0.0000022481, "kilograms-force": value * 0.0000010197},
            "pounds-force": {"newtons": value * 4.44822, "dynes": value * 444822, "kilograms-force": value * 0.453592},
            "kilograms-force": {"newtons": value * 9.80665, "dynes": value * 980665, "pounds-force": value * 2.20462},
        }
    }
    
    return conversion_factors.get(category, {}).get(from_unit, {}).get(to_unit, "Conversion not available")

# Convert button
if st.button("Convert", key="convert", help="Click to convert the units"):
    with st.spinner("Converting..."):
        time.sleep(1)  # Simulating processing time
        result = convert_units(value, from_unit, to_unit, category)
        st.markdown(f'<div class="result-box">{value} {from_unit} = {result} {to_unit}</div>', unsafe_allow_html=True)

# Footer with your name
st.markdown('<p class="footer">🚀 Made by <b>Ali Hassan</b></p>', unsafe_allow_html=True)
