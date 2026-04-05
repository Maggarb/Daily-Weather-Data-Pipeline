import sqlite3
import logging
from pathlib import Path

DB_PATH = Path("data/weather.db")


def load_weather(data):
    try:
        logging.info("Loading data into SQLite")

        # connect (creates DB if missing)
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # create table if not exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            latitude REAL,
            longitude REAL,
            temperature REAL,
            windspeed REAL
        )
        """)

        # insert data
        cursor.execute("""
        INSERT INTO weather (
            timestamp,
            latitude,
            longitude,
            temperature,
            windspeed
        )
        VALUES (?, ?, ?, ?, ?)
        """, (
            data["timestamp"],
            data["latitude"],
            data["longitude"],
            data["temperature"],
            data["windspeed"]
        ))

        conn.commit()
        conn.close()

        logging.info("Data saved to SQLite successfully")

    except Exception as e:
        logging.error(f"SQLite load failed: {e}")
        raise