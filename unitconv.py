import streamlit as st
import requests

# Set page configuration
st.set_page_config(
    page_title="Smart Converter",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Application title
st.sidebar.title("Smart Converter")

# Unit conversion factors
conversion_factors = {
    "Length": {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
        "Inch": 39.3701, "Foot": 3.28084, "Yard": 1.09361, "Mile": 0.000621371
    },
    "Weight": {
        "Gram": 1, "Kilogram": 0.001, "Milligram": 1000, "Pound": 0.00220462,
        "Ounce": 0.035274, "Ton": 1e-6
    },
    "Volume": {
        "Liter": 1, "Milliliter": 1000, "Cubic Meter": 0.001,
        "Gallon": 0.264172, "Quart": 1.05669, "Pint": 2.11338, "Cup": 4.22675
    },
    "Temperature": {},  # Special case
    "Area": {
        "Square Meter": 1, "Square Kilometer": 0.000001, "Square Centimeter": 10000,
        "Square Inch": 1550, "Square Foot": 10.7639, "Acre": 0.000247105, "Hectare": 0.0001
    },
    "Time": {
        "Second": 1, "Millisecond": 1000, "Minute": 1/60, "Hour": 1/3600,
        "Day": 1/86400, "Week": 1/604800, "Month": 1/2.628e+6, "Year": 1/3.154e+7
    },
    "Data": {
        "Byte": 1, "Kilobyte": 1/1024, "Megabyte": 1/(1024**2), "Gigabyte": 1/(1024**3),
        "Terabyte": 1/(1024**4), "Bit": 8
    },
    "Speed": {
        "Meter per Second": 1, "Kilometer per Hour": 3.6, "Mile per Hour": 2.23694, "Knot": 1.94384
    }
}

# API function to get currency rates
def get_currency_rates():
    """Get real-time currency rates using a free API"""
    CURRENCY_API_URL = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(CURRENCY_API_URL)
    data = response.json()
    rates = data["rates"]
    rates["timestamp"] = data["time_last_update_utc"]
    return rates

# Sidebar for converter selection
st.sidebar.subheader("Choose Converter")
converter_type = st.sidebar.radio("Converter Type", ["Unit Converter", "Currency Converter"])

# Main content area
st.title("Smart Converter")

st.subheader("Convert with Selection")

if converter_type == "Unit Converter":
    category = st.selectbox(
        "Select Measurement Category",
        ["Length", "Weight", "Volume", "Temperature", "Area", "Time", "Data", "Speed"]
    )

    col1, col2 = st.columns(2)

    with col1:
        from_unit = st.selectbox("From Unit", list(conversion_factors[category].keys()) if category != "Temperature" else ["Celsius", "Fahrenheit", "Kelvin"])
        value = st.number_input("Enter Value", value=1.0, step=0.1)

    with col2:
        to_unit = st.selectbox("To Unit", list(conversion_factors[category].keys()) if category != "Temperature" else ["Celsius", "Fahrenheit", "Kelvin"])

    if st.button("Convert Units"):
        if category == "Temperature":
            if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    result = (value * 9/5) + 32
                elif to_unit == "Kelvin":
                    result = value + 273.15
                else:
                    result = value
            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    result = (value - 32) * 5/9
                elif to_unit == "Kelvin":
                    result = (value - 32) * 5/9 + 273.15
                else:
                    result = value
            elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    result = value - 273.15
                elif to_unit == "Fahrenheit":
                    result = (value - 273.15) * 9/5 + 32
                else:
                    result = value
        else:
            # Perform unit conversion using the conversion factor
            result = value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])

        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

else:  # Currency Converter
    with st.spinner("Getting latest currency rates..."):
        rates = get_currency_rates()
        currencies = [k for k in rates.keys() if k != "timestamp"]
        last_updated = rates["timestamp"]

    st.caption(f"Exchange rates last updated: {last_updated}")

    col1, col2 = st.columns(2)

    with col1:
        from_currency = st.selectbox("From Currency", currencies)
        amount = st.number_input("Enter Amount", value=1.0, step=0.1)

    with col2:
        to_currency = st.selectbox("To Currency", currencies)

    if st.button("Convert Currency"):
        if from_currency in rates and to_currency in rates:
            converted_amount = (amount / rates[from_currency]) * rates[to_currency]
            st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            st.error("Invalid currency selection.")
