import pandas as pd
import sqlite3

df = pd.read_csv("sample_data.csv")

df = df.dropna()
df = df[df["amount"] != 0]

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER,
    name TEXT,
    amount REAL,
    date TEXT
)
""")

df.to_sql("transactions", conn, if_exists="append", index=False)

print("Records inserted:", len(df))

conn.close()
