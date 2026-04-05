from datetime import datetime

def transform_weather(data):
    weather = data["current_weather"]

    return {
        "timestamp": datetime.fromisoformat(weather["time"]).isoformat(),
        "latitude": data["latitude"],
        "longitude": data["longitude"],
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"]
    }