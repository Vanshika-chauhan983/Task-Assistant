# Task Assistant (Gemini-Powered CLI)

A smart CLI-based task management assistant that lets you create and manage tasks using natural language — powered by Google's Gemini 1.5-flash and backed by SQLite.

---

## Features

### Task Management via Natural Language
- Add tasks like:
  > "Add a task to buy books by Monday, high priority, category college"

### Core Features
- Add, list, update, delete tasks
- Track task `status` (pending/completed)
- Priority, due date, category detection from natural text
- Filter tasks by `priority`, `category`, or `status`

### NLP-Powered Assistant (Gemini-1.5-flash)
- Uses Gemini API to extract structured task data
- Parses free-form input into title, priority, category, and  due date

### Productivity Tools
- **Daily Reminder** system (scheduled task summary at 9 AM)
- CSV **report generation**
- Task breakdown by filters (priority, category or status)

---

## Setup Guide

### 1. Clone the Repo

git clone https://github.com/Vanshika-chauhan983/Task-Assistant.git

cd task-assistant

### 2. Install Requirements

pip install -r requirements.txt

### 3. Set Up Environment

Create a .env file in the root folder with your Gemini API key.

GEMINI_API_KEY=your_gemini_key_here

### 4. Initialize the Database

python setup.py

This creates tasks.db and prepares the schema.

## Usage Examples

### 1. Add a Task

python main.py

**Prompt:**
Add a task to buy milk by 17-07-2025, high priority, category personal

**Result:**

Gemini Raw Output-

{"title": "buy milk", "priority": "high", "due_date": "17-07-2025", "category": "personal"}

Task added to the database.

### 2. List tasks 

python main.py

**Prompt:**
List tasks

**Result:**

Task List:

ID: 1

Title:     Complete assignment

Priority:  01-07-2025

Due Date:  high

Category:  college

Status: pending

------------------------------
ID: 2

Title:     Buy groceries

Priority:  Monday

Due Date:  None

Category:  None

Status: pending

------------------------------
ID: 3

Title:     Buy gift

Priority:  Tuesday

Due Date:  high

Category:  personal

Status: Completed

------------------------------

### 3. Filter Tasks

python main.py

**Prompt:**
Filter tasks

Status (leave blank for any type):

Category (leave blank for any type): college

Priority (leave blank for any):

**Result:**

ID: 1

Title: Complete assignment

Priority: 01-07-2025

Due Date: high

Category: college

Status: pending

------------------------------
ID: 4

Title: Complete Data Science project

Priority: Sunday

Due Date: high

Category: college

Status: pending

------------------------------

### 4. Update Task

python main.py

**Prompt:**
Enter the task ID to update: 5

New title (leave blank to keep current title): Find Internship

New due date (leave blank to keep current due date):

New priority (leave blank to keep current priority):

New category (leave blank to keep current category):

Enter the status of task: completed

**Result:**
Task updated successfully.

### 5. Delete Task

python main.py

**Prompt:**
Delete task

Enter the task ID to delete:5

**Result:**
Task 5 deleted successfully.

### 6. Export Tasks as CSV

python main.py

**Prompt:**
Export as CSV

**Result:**
Tasks exported to tasks_report.csv.

### 7. Daily Reminder

Schedule a daily CLI reminder at 9AM.

python reminder.py

**Result:**
Daily Task Summary (2025-06-29)

Complete assignment (high priority) by 01-07-2025

Buy groceries (None priority) by Monday

Complete Data Science project (high priority) by Sunday

Find Internship (25-07-2025 priority) by high

Buy milk (high priority) by 17-07-2025

## Project Structure

task-assistant/

├── core/

│   └── task_manager.py       # DB operations

├── main.py                   # CLI logic

├── gemini_parser.py          # Gemini NLP parser

├── reminder.py               # Scheduled daily reminders

├── setup.py                  # Initializes the DB

├── tasks.db                  # SQLite database

├── .env                      # API key (not shared)

├── requirements.txt          # Dependencies

└── README.md       

## Requirements

Python 3.8+

google-generativeai

python-dotenv

schedule

Install with:

pip install -r requirements.txt

## Author

**Vanshika Chauhan**

Built as a part of an internship Project submission - June 2025
