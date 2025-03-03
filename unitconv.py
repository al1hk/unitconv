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
st.markdown('<p class="title">🔄 Modern Unit Converter</p>', unsafe_allow_html=True)

# Input fields
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# Dropdown selections for units
units = ["meters", "kilometers", "centimeters", "miles"]
col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("From", units)

with col2:
    to_unit = st.selectbox("To", units)

# Conversion logic
def convert_units(value, from_unit, to_unit):
    conversions = {
        "meters": {"kilometers": value / 1000, "centimeters": value * 100, "miles": value * 0.000621371},
        "kilometers": {"meters": value * 1000, "centimeters": value * 100000, "miles": value * 0.621371},
        "centimeters": {"meters": value / 100, "kilometers": value / 100000, "miles": value * 0.0000062137},
        "miles": {"meters": value / 0.000621371, "kilometers": value / 0.621371, "centimeters": value / 0.0000062137},
    }
    return conversions.get(from_unit, {}).get(to_unit, "Conversion not available")

# Convert button
if st.button("Convert", key="convert", help="Click to convert the units"):
    with st.spinner("Converting..."):
        time.sleep(1)  # Simulating processing time
        result = convert_units(value, from_unit, to_unit)
        st.markdown(f'<div class="result-box">{value} {from_unit} = {result} {to_unit}</div>', unsafe_allow_html=True)

# Footer with your name
st.markdown('<p class="footer">🚀 Made by <b>Ali Hassan</b></p>', unsafe_allow_html=True)
