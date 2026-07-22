import sqlite3

conn = sqlite3.connect("demo.db")
# connects to a db [creates a db if db does not exists]
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(20) ,
            des  TEXT
               )
    ''')

conn.close()


def addtasks():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    name = input('enter taskname : -')
    des = input("enter task description : - ")
    cursor.execute('''
        INSERT INTO Tasks(name,des)
                   VALUES(?,?)
    ''', (name, des))
    print("TAsk added ✅")
    conn.commit()
    conn.close()

def viewtask():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Tasks
    ''')
    tasks = cursor.fetchall() #retreives list of  data from the last executes querry
    print("TASKS found")
    print("____________________")
    for i in tasks:
        print(f"task {i[0]} - {i[1]}")


def search_task():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    task_id= int(input("enter task id : - "))
    cursor.execute('''
        SELECT * FROM Tasks WHERE id = ?   
    ''',(task_id,))
    task = cursor.fetchone()
    if task:
        print("task found ")
        print(f"task {task[0]} - {task[1]}")
        
    else:
        print("no such task ")

def update_task():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    td = int(input("Enter the task id :- "))
    tname = input("Enter the task name :- ")
    tdes= input("Enter task des :- ")
    cursor.execute(
        """
        UPDATE tasks SET name = ? ,des = ? WHERE id = ?
        """, (tname,tdes,td)
    )
    conn.commit()
    print("Task Completed")

def delete_task():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    tid = int(input("Enter the task id :- "))
    ch = input("Are you Sure you want to delete Y/N :-").lower()
    if ch == "y":
        cursor.execute(
            """
            DELETE FROM tasks WHERE id = ?
            """,(tid,)
        )
        conn.commit()
        print("Task Deleted ")
    else:
        print("Task Not Deleted")


def main():
    while True:
        print("welcome to task management ")
        ch = int(input("1.add task\n2.view task\n3.search tasks\n4.update tasks\n5.delete tasks\n6.exit \n: -"))
        if ch == 1:
            addtasks()
        elif ch == 2:
            viewtask()
        elif ch == 3:
            search_task()
        elif ch == 4:
            update_task()
        elif ch == 5:
            delete_task()
        elif ch == 6:
            break
        else:
            print("invalid input")

main()


# create an employee
# neeed to add 
# needed to view
# needed to search

