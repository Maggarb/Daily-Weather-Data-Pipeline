from extract import extract_weather
from transform import transform_weather
from load import load_weather

def run():
    raw = extract_weather()
    clean = transform_weather(raw)
    load_weather(clean)
    print("Pipeline executed successfully!")

if __name__ == "__main__":
    run()