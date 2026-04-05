import sqlite3

conn = sqlite3.connect("data/weather.db")
cursor = conn.cursor()

rows = cursor.execute("SELECT * FROM weather").fetchall()

for r in rows:
    print(r)

conn.close()