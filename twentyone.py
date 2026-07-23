import sqlite3

conn = sqlite3.connect('book.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS author(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(20) ,
            details  TEXT
               )
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author_id INTEGER ,
        Name VARCHAR(20) UNIQUE,
        Price INTEGER ,
        FOREIGN KEY(author_id) REFERENCES author(id)
        )
    ''')


def add_data():
    conn = sqlite3.connect("book.db")
    cursor = conn.cursor()
    name  = input("Enter the name :- ")
    deta = input("Enter the Password :- ")
    cursor.execute(
        """
        INSERT INTO Datas (name , password )
        VALUES(?,?)
        """, (name,deta)
    )
    conn.commit()
    conn.close()
    print("Data Added Sucessfully\n")

