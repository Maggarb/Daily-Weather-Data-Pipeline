import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("data/weather.db")

df = pd.read_sql("SELECT * FROM weather", conn)

df["time"] = pd.to_datetime(df["time"])

plt.plot(df["time"], df["temperature"])
plt.title("Temperature Over Time")
plt.xticks(rotation=45)
plt.show()