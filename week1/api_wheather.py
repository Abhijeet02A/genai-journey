import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 17,
    "longitude": 78,
    "current_weather": True
}

response = requests.get(url, params=params)

print(response.status_code)
data = response.json()
print(data)