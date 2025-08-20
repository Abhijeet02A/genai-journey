import datetime
from zoneinfo import ZoneInfo
import streamlit as st
import requests

# To Run  - Path to the file streamlit run filename.py      

# Predefined city coordinates

city_coords = {
    "Hyderabad": (17.385, 78.4867),
    "Chennai": (13.0827, 80.2707),
    "Bengaluru": (12.9716, 77.5946)
}

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data["current_weather"]
    except Exception as e:
        st.error(f"Error fetching weather: {e}")
        return None

st.title("🌦️ Weather Forecast App")

city = st.selectbox("Select a city", list(city_coords.keys()))

if st.button("Get Weather"):
    weather = get_weather(*city_coords[city])
    if weather:
        st.write(f"**Time:** {weather['time']}")
        st.write(f"**Temperature:** {weather['temperature']}°C")
        st.write(f"**Wind Speed:** {weather['windspeed']} km/h")
        st.write(f"**Weather Code:** {weather['weathercode']}")
