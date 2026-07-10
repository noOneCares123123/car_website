import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    brand TEXT,
    year INTEGER,
    horsepower INTEGER,
    engine TEXT,
    topspeed INTEGER,
    image TEXT,
    description TEXT
)
""")

conn.commit()
conn.close()

print("Database created!")