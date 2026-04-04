from datetime import datetime

def transform_weather(data):
    weather = data["current_weather"]

    return {
        "time": datetime.now().isoformat(),
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"]
    }