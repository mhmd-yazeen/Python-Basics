import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Datas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(20) ,
            password  TEXT
               )
    ''')

def add_data():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    name  = input("Enter the name :- ")
    passw = input("Enter the Password :- ")
    cursor.execute(
        """
        INSERT INTO Datas (name , password )
        VALUES(?,?)
        """, (name,passw)
    )
    conn.commit()
    conn.close()
    print("Data Added Sucessfully\n")

def view_data():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM Datas 
        """
    )
    datas = cursor.fetchall()
    print("\n\tData Founded")
    print("-------------------------------")
    for i in datas:
        print(f'datas  {i[0]}  -  {i[1]}')

def update_data():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()  
    did = int(input("Enter the data id :- "))
    dname = input("Enter the New name :-")
    dpass = input("Enter the New password :-")
    cursor.execute(
        """
        UPDATE Datas SET name = ? ,password = ? WHERE id = ?
        """, (dname,dpass,did)
    )
    conn.commit()
    print("Data Updated Sucessfully\n")

def delete_data():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    did = int(input("Enter the Data Id :-"))
    ch = input("Are you sure you want to delete Y/N :-").upper()
    if ch == "Y":
        cursor.execute(
            """
            DELETE FROM Datas WHERE id = ?
            """, (did,)
        )
        conn.commit()
        print("Data Deleted !")
    else:
        print("Data Not Deleted")


def main():
    while True:
        print("\t\tWelcome To Data Base")
        ch = int(input("1.Add Data \n2.View Data \n3.Update Data \n4.Delete Data \n5.Exit\n"))
        if ch == 1:
            add_data()
        elif ch == 2:
            view_data()
        elif ch == 3:
            update_data()
        elif ch == 4:
            delete_data()
        else:
            print("Invalid Choice")

main()