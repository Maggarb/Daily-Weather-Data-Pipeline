import logging
from utils.logger import setup_logger


from pipeline.extract import extract_weather
from pipeline.transform import transform_weather
from pipeline.load import load_weather

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