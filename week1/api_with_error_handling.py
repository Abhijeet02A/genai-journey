import requests

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

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

weather = get_weather(17.419755589930347, 78.35022369262157)

city_coords = {
    "Hyderabad": (17.419550854195656, 78.34973016617259),
    "Chennai": (13.097902593563383, 80.17112331632858),
    "Bengaluru": (12.97848955041603, 77.54839899378507)
}
for city, coordinates in city_coords.items():
    print(f"Weather in '{city}'", get_weather(coordinates[0], coordinates[1]))
    print()
    
