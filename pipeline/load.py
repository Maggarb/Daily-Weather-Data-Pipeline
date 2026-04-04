import sqlite3

def load_weather(record):
    conn = sqlite3.connect("data/weather.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            time TEXT,
            temperature REAL,
            windspeed REAL
        )
    """)

    cursor.execute(
        "INSERT INTO weather VALUES (?, ?, ?)",
        (record["time"], record["temperature"], record["windspeed"])
    )

    conn.commit()
    conn.close()