import sqlite3
import csv

def init_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            due_date TEXT,
            priority TEXT,
            category TEXT,
            status TEXT DEFAULT 'pending',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()

def add_task(title, priority=None, due_date=None, category=None ):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO task (title, due_date, priority, category)
        VALUES (?, ?, ?, ?)
    """, (title, due_date, priority, category))
    conn.commit()
    conn.close()

def list_allTasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        print("No tasks found.")
    else:
        print("\nTask List:\n")
        for task in tasks:
            print(f"ID: {task[0]}")
            print(f"Title:     {task[1]}")
            print(f"Priority:  {task[2]}")
            print(f"Due Date:  {task[3]}")
            print(f"Category:  {task[4]}")
            print(f"Status: {task[5]}")
            print("-" * 30)

def list_tasks(status=None, category=None, priority=None):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    query ="SELECT * FROM task where 1=1"
    params=[]

    if status:
        query += " AND status = ?"
        params.append(status)
    if category:
        query += " AND category = ?"
        params.append(category)
    if priority:
        query += " AND priority = ?"
        params.append(priority)

    cursor.execute(query,tuple(params))
    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"ID: {task[0]}")
            print(f"Title: {task[1]}")
            print(f"Priority: {task[2]}")
            print(f"Due Date: {task[3]}")
            print(f"Category: {task[4]}")
            print(f"Status: {task[5]}")
            print("-"*30)

def update_task(task_id, new_title=None, new_priority=None, new_due_date=None, new_category=None, new_status=None):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM task Where id = ?", (task_id,))
    task = cursor.fetchone()
    if not task:
        print(f"No such task found.")
        conn.close()
        return
    
    updated_title=new_title if new_title else task[1]
    updated_priority=new_priority if new_priority else task[2]
    updated_due_date=new_due_date if new_due_date else task[3]
    updated_category=new_category if new_category else task[4]
    updated_status=new_status if new_status else task[5]

    cursor.execute("UPDATE task SET title = ?, due_date= ?,priority = ?, category=?, status=? WHERE id = ?", (updated_title, updated_due_date, updated_priority, updated_category, updated_status, task_id))
    conn.commit()
    conn.close()
    print(f"Task updated successfully.")

def delete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM task WHERE id = ?", (task_id,))
    task = cursor.fetchone()

    if not task:
        print(f"No task found with ID {task_id}")
    else:
        cursor.execute("DELETE FROM task WHERE id = ?", (task_id,))
        conn.commit()
        print(f"Task {task_id} deleted successfully.")
    conn.close()

def export_tasks_to_csv(filename="tasks_report.csv"):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()
    conn.close()

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Title', 'Priority', 'Due Date', 'Category', 'Status'])
        writer.writerows(tasks)

    print(f"Tasks exported to {filename}.")