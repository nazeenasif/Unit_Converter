import streamlit as st

# Apply custom CSS for background color and border
st.markdown(
    """
    <style>
    .stApp {
        background-color: lightblue;  /* Light blue background */
    }
    
    .stTextInput, .stNumberInput, .stSelectbox {
        border: 5px solid darkblue;
        border-radius: 10px;
        padding: 10px;
    }

    .stButton > button {
        border: 3px solid darkgreen;
        border-radius: 10px;
        padding: 10px;
        color: white;
        background-color: darkgreen;
        width: 120px;
    }

    .result-text {
        font-size: 32px;
        font-weight: bold;
    }
    
    .stTitle {
        color: darkblue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def convert_unit(value, unit_from, unit_to):
    conversions = {
        "length" : {
            "meter_to_kilometer": 0.001,
            "kilometer_to_meter": 1000,
            "kilometer_to_centimeter": 100000,
            "centimeter_to_kilometer": 0.00001,
            "meter_to_centimeter": 100,
            "centimeter_to_meter": 0.01,
            "inch_to_centimeter": 2.54,
            "centimeter_to_inch": 0.393701,
            "foot_to_meter": 0.3048,
            "meter_to_foot": 3.28084,
            "mile_to_kilometer": 1.60934,
            "kilometer_to_mile": 0.621371,
        },
        "weight" : {
            "gram_to_kilogram": 0.001,
            "kilogram_to_gram": 1000,
            "pound_to_kilogram": 0.453592,
            "kilogram_to_pound": 2.20462,
            "pound_to_gram": 453.592,
            "gram_to_pound": 0.00220462,
        },
        "temperature" : {
            "celsius_to_fahrenheit": 1.8,
            "fahrenheit_to_celsius": 0.555556,
            "kelvin_to_celsius": -273.15,
            "celsius_to_kelvin": 273.15,
            "fahrenheit_to_kelvin": 255.372,
            "kelvin_to_fahrenheit": 32.0,
        },
        "time" : {
            "second_to_minute": 1/60,
            "minute_to_second": 60,
            "minute_to_hour": 1/60,
            "hour_to_minute": 60,
            "second_to_hour": 1/3600,
            "hour_to_second": 3600,
            "second_to_day": 1/86400,
            "day_to_second": 86400,
            "second_to_year": 1/31536000,
            "year_to_second": 31536000,
        },
        "volume" : {
            "liter_to_gallon": 0.264172,
            "gallon_to_liter": 3.78541,
            "liter_to_milliliter": 1000,
            "milliliter_to_liter": 0.001,
            "milliliter_to__gallon": 0.000264172,
        }
    } 
    
    for category, conversions_dict in conversions.items() :
        if f"{unit_from}_to_{unit_to}" in conversions_dict :
            conversion = conversions_dict[f"{unit_from}_to_{unit_to}"]
            return conversion(value) if callable(conversion) else value * conversion
    return "Unit conversion not supported."

st.title("Unit Converter🔁📏")

# Fix unit names to match conversion keys
categories = {
    "Length": ["meter", "kilometer", "centimeter", "inch", "foot", "mile"],
    "Weight": ["gram", "kilogram", "pound"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day", "year"],
    "Volume": ["liter", "gallon", "milliliter"] 
}

category = st.selectbox("Select a category :", list(categories.keys()))
units = categories[category]

value = st.number_input("Enter the Value:", min_value=1.0, step=1.0)

unit_from = st.selectbox("Convert from:", units)
unit_to = st.selectbox("Convert to:", units)

if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.markdown(f'<p class="result-text">Converted value: {result}</p>', unsafe_allow_html=True)
    
st.markdown("---")
st.markdown("🚀 Developed by **Nazeen Asif**")
