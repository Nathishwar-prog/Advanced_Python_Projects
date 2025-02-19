# Advanced  Task Manager
# Author : Nathishwar

import time as t
from datetime import datetime

class Task:
    def __init__(self, description, priority="Medium", due_date=None, category=None):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.category = category
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        due_date_str = f", Due: {self.due_date.strftime('%Y-%m-%d')}" if self.due_date else ""
        category_str = f", Category: {self.category}" if self.category else ""
        return f"{self.description} [Priority: {self.priority}{due_date_str}{category_str}] - {status}"

class ToDoList:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        if task in self.tasks:
            print("Task already exists!")
            return False
        else:
            self.tasks.append(task)
            return True

    def delete_task(self, task_index):
        try:
            self.tasks.pop(task_index - 1)
            return True
        except IndexError:
            print("You entered an out-of-range index!")
            return False

    def mark_task_completed(self, task_index):
        try:
            self.tasks[task_index - 1].completed = True
            return True
        except IndexError:
            print("You entered an out-of-range index!")
            return False

    def show_tasks(self, show_completed=False):
        print("Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            if not task.completed or show_completed:
                print(f"{i}. {task}")

    def search_tasks(self, keyword):
        print(f"Search results for '{keyword}':")
        for i, task in enumerate(self.tasks, start=1):
            if keyword.lower() in task.description.lower():
                print(f"{i}. {task}")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                due_date_str = task.due_date.strftime('%Y-%m-%d') if task.due_date else ""
                file.write(f"{task.description}|{task.priority}|{due_date_str}|{task.category}|{task.completed}\n")
        print("Tasks saved successfully!")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = []
                for line in file:
                    description, priority, due_date_str, category, completed = line.strip().split('|')
                    due_date = datetime.strptime(due_date_str, '%Y-%m-%d') if due_date_str else None
                    task = Task(description, priority, due_date, category)
                    task.completed = completed == 'True'
                    self.tasks.append(task)
            print("Tasks loaded successfully!")
        except FileNotFoundError:
            print("No saved tasks found.")

if __name__ == "__main__":
    tsk = ToDoList("My To Do List")
    while True:
        t.sleep(1)
        print("*" * 10, "To Do List", "*" * 10)
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Show Tasks")
        print("5. Search Tasks")
        print("6. Save Tasks")
        print("7. Load Tasks")
        print("8. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            description = input("Enter Task Description: ")
            priority = input("Enter Priority (High/Medium/Low): ").capitalize()
            due_date_str = input("Enter Due Date (YYYY-MM-DD, optional): ")
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d') if due_date_str else None
            category = input("Enter Category (optional): ")
            task = Task(description, priority, due_date, category)
            if tsk.add_task(task):
                t.sleep(1)
                print("Processing....")
                t.sleep(2)
                print("Task Added Successfully!")
        elif ch == 2:
            task_index = int(input("Enter task number to delete: "))
            if tsk.delete_task(task_index):
                t.sleep(1)
                print("Processing....")
                t.sleep(2)
                print("Task Deleted Successfully!")
        elif ch == 3:
            task_index = int(input("Enter task number to mark as completed: "))
            if tsk.mark_task_completed(task_index):
                t.sleep(1)
                print("Processing....")
                t.sleep(2)
                print("Task Marked as Completed!")
        elif ch == 4:
            t.sleep(1)
            print("Processing....")
            t.sleep(2)
            show_completed = input("Show completed tasks? (yes/no): ").lower() == 'yes'
            tsk.show_tasks(show_completed)
        elif ch == 5:
            keyword = input("Enter keyword to search: ")
            tsk.search_tasks(keyword)
        elif ch == 6:
            filename = input("Enter filename to save tasks: ")
            tsk.save_tasks(filename)
        elif ch == 7:
            filename = input("Enter filename to load tasks: ")
            tsk.load_tasks(filename)
        elif ch == 8:
            break
        else:
            print("Please enter a valid choice!")
