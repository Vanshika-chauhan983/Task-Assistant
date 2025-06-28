import sqlite3
import time
import schedule
from datetime import datetime

def show_daily_summary():
    conn=sqlite3.connect("tasks.db")
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM task WHERE status='pending'")
    tasks=cursor.fetchall()
    conn.close()

    print("\n Daily Task Summary (" + datetime.now().strftime("%Y-%m-%d") + ")")
    if tasks:
        for task in tasks:
            print(f"{task[1]} ({task[3]} priority) by {task[2]}")
    else:
        print("No pending tasks for today!")

schedule.every().day.at("02:30").do(show_daily_summary)
while True:
    schedule.run_pending()
    time.sleep(1)