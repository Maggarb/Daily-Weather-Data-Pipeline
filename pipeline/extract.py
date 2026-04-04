import requests

def extract_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 64.1466,
        "longitude": -21.9426,
        "current_weather": True
    }

    response = requests.get(url, params=params)
    return response.json()