import logging
from utils.logger import setup_logger
from dotenv import load_dotenv
import os

from pipeline.extract import extract_weather
from pipeline.transform import transform_weather
from pipeline.load import load_weather

# Load environment variables
load_dotenv()

# Get coordinates from .env
LAT = float(os.getenv("LATITUDE"))
LON = float(os.getenv("LONGITUDE"))


setup_logger()

def run():
    try:
        logging.info("Pipeline started")

        raw = extract_weather()
        clean = transform_weather(raw)
        load_weather(clean)

        logging.info("Pipeline finished successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run()