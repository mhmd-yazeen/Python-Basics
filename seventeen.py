# Database
# resource containing data
# data - info

# Relational database - data is stored in tables
# Sql - structured query language
# Example: MySQL, PostgreSQL

# Non-relational database - data is stored in a non-tabular form
# example: MongoDB, 


import sqlite3
conn = sqlite3.connect("First.db") # Establishing an connection to db
# cursor = conn.cursor() # interact with the db
# cursor.execute(
#     """ 
#     CREATE TABLE IF NOT EXIST Student(
#     name VARCHAR(20),
#     age INTEGER,
#     address TEXT
#     )
#     """
# )

# cursor.execute(
#     """
#     INSERT INTO Student (name,age,address)
#     VALUES('John', 20, 'Kottayam')
#     """
# )

def addstudent():
    conn = sqlite3.connect("First.db")
    cursor = conn.cursor() 
    student_name = input("Enter student name :- ")
    student_age = int(input("Enter Student age :- "))
    student_address = input("Enter Student Address :- ")
    cursor.execute("""
    INSERT INTO Student(name,age,address)
        VALUES(?,?,?)
        """,(student_name,student_age,student_address))
    conn.commit()
    print("Student Added ✅")

conn.close()


def main():
    while True:
        print("Welcome to Database")
        ch = int(input("1.ADD Details\n2.VIEW Details"))
        if ch == 1:
            addstudent()
        else:
            print("Invalid Choice")

main()
