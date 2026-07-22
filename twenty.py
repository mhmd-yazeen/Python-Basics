import sqlite3

conn = sqlite3.connect ("demo.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(20) UNIQUE ,
            des  TEXT
               )
    ''')

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        name VARCHAR(20),
        des TEXT,
        FOREIGN KEY(user_id) REFERENCES Users(id)
    )
""")

