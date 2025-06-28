from gemini_parser import parse_task
from core.task_manager import add_task, list_tasks, update_task, delete_task, export_tasks_to_csv, list_allTasks

print("\n Task Assistant CLI with Gemini\n")

user_input = input("Enter your command:\n> ")

if user_input.lower().startswith("add"):
    task_data = parse_task(user_input)
    if task_data:
        add_task(
            title=task_data.get("title"),
            priority=task_data.get("priority"),
            due_date=task_data.get("due_date"),
            category=task_data.get("category")
        )
        print("Task added to the database.")
    else:
        print("Could not parse task from input.")

elif user_input.lower().startswith("list"):
    list_allTasks()

elif user_input.lower().startswith("filter tasks"):
    status=input("Status (leave blank for any type): ").strip() or None
    category=input("Category (leave blank for any type): ").strip() or None
    priority = input("Priority (leave blank for any): ").strip() or None
    list_tasks(status=status,category=category,priority=priority)

elif user_input.lower().startswith("update"):
    task_id=int(input("Enter the task ID to update: "))
    new_title=input("New title (leave blank to keep current title): ")
    new_due_date = input("New due date (leave blank to keep current due date): ")
    new_priority=input("New priority (leave blank to keep current priority): ")
    new_category = input("New category (leave blank to keep current category): ")
    new_status=input("Enter the status of task: ")
    update_task(task_id, new_title, new_due_date, new_priority, new_category, new_status)

elif user_input.lower().startswith("delete"):
    task_id=int(input("Enter the task ID to delete: "))
    delete_task(task_id)

elif user_input.lower().startswith("export"):
    export_tasks_to_csv()

else:
    print("Unknown command.")