# Advanced_Python_Projects
This projects are enhanced by some additional features and more functionality . I give the assurance this are in unique ways of projects.

# Task-Manager(like To-Do-List )
# **Project Report: Advanced To-Do List Application**

---

## **Author: Nathishwar**

---

## **Table of Contents**
1. **Introduction**
2. **Features**
3. **Class Design**
4. **Functionality**
   - Add Task
   - Delete Task
   - Mark Task as Completed
   - Show Tasks
   - Search Tasks
   - Save Tasks
   - Load Tasks
5. **Code Explanation**
6. **Usage**
7. **Future Enhancements**
8. **Conclusion**

---

## **1. Introduction**
The **Advanced To-Do List Application** is a Python-based program designed to help users manage their tasks efficiently. It provides a user-friendly interface with advanced features such as task prioritization, due dates, task categorization, and the ability to save and load tasks to/from a file. This project is developed as a command-line application and is suitable for personal task management.

---

## **2. Features**
The application includes the following features:
1. **Add Task**: Users can add tasks with a description, priority, due date, and category.
2. **Delete Task**: Users can delete tasks by specifying the task number.
3. **Mark Task as Completed**: Users can mark tasks as completed.
4. **Show Tasks**: Users can view all tasks, including completed and incomplete ones.
5. **Search Tasks**: Users can search for tasks using keywords.
6. **Save Tasks**: Users can save their tasks to a file for future use.
7. **Load Tasks**: Users can load previously saved tasks from a file.

---

## **3. Class Design**
The program is designed using object-oriented programming (OOP) principles. The main classes are:

### **1. `Task` Class**
- Represents a single task.
- **Attributes**:
  - `description`: Description of the task.
  - `priority`: Priority of the task (High/Medium/Low).
  - `due_date`: Due date of the task (optional).
  - `category`: Category of the task (optional).
  - `completed`: Completion status of the task (`True` or `False`).
- **Methods**:
  - `__str__`: Returns a string representation of the task.

### **2. `ToDoList` Class**
- Represents the to-do list and manages all tasks.
- **Attributes**:
  - `name`: Name of the to-do list.
  - `tasks`: List of `Task` objects.
- **Methods**:
  - `add_task`: Adds a new task to the list.
  - `delete_task`: Deletes a task by its index.
  - `mark_task_completed`: Marks a task as completed.
  - `show_tasks`: Displays all tasks.
  - `search_tasks`: Searches for tasks by keyword.
  - `save_tasks`: Saves tasks to a file.
  - `load_tasks`: Loads tasks from a file.

---

## **4. Functionality**

### **1. Add Task**
- Users can add a task by providing:
  - Description
  - Priority (High/Medium/Low)
  - Due date (optional)
  - Category (optional)
- The task is added to the list if it doesn't already exist.

### **2. Delete Task**
- Users can delete a task by specifying its index.
- The program ensures the index is valid.

### **3. Mark Task as Completed**
- Users can mark a task as completed by specifying its index.
- The program ensures the index is valid.

### **4. Show Tasks**
- Users can view all tasks, including their:
  - Description
  - Priority
  - Due date
  - Category
  - Completion status
- Users can choose to show completed tasks or only incomplete ones.

### **5. Search Tasks**
- Users can search for tasks by entering a keyword.
- The program displays tasks whose descriptions contain the keyword.

### **6. Save Tasks**
- Users can save their tasks to a file.
- Tasks are saved in a structured format, with each task's details separated by a pipe (`|`).

### **7. Load Tasks**
- Users can load tasks from a previously saved file.
- The program reconstructs the `Task` objects from the file.

---

## **5. Code Explanation**

### **Key Functions**

#### **1. `save_tasks`**
- Saves tasks to a file.
- Each task is written in the format:
  ```
  description|priority|due_date|category|completed
  ```
- Example:
  ```
  Buy groceries|High|2023-10-15|Personal|False
  ```

#### **2. `load_tasks`**
- Loads tasks from a file.
- Parses each line to reconstruct the `Task` objects.
- Handles cases where the file doesn't exist.

---

## **6. Usage**

### **Running the Program**
1. Run the script in a Python environment.
2. The main menu will be displayed with the following options:
   ```
   1. Add Task
   2. Delete Task
   3. Mark Task as Completed
   4. Show Tasks
   5. Search Tasks
   6. Save Tasks
   7. Load Tasks
   8. Exit
   ```
3. Follow the on-screen prompts to perform actions.

### **Example Workflow**
1. Add a task:
   ```
   Enter Task Description: Buy groceries
   Enter Priority (High/Medium/Low): High
   Enter Due Date (YYYY-MM-DD, optional): 2023-10-15
   Enter Category (optional): Personal
   ```
2. Show tasks:
   ```
   Tasks:
   1. Buy groceries [Priority: High, Due: 2023-10-15, Category: Personal] - Incomplete
   ```
3. Save tasks to a file:
   ```
   Enter filename to save tasks: my_tasks.txt
   Tasks saved successfully!
   ```
4. Load tasks from a file:
   ```
   Enter filename to load tasks: my_tasks.txt
   Tasks loaded successfully!
   ```

---

## **7. Future Enhancements**
1. **User Authentication**: Add user login functionality to manage multiple users' tasks.
2. **Graphical User Interface (GUI)**: Develop a GUI using libraries like Tkinter or PyQt.
3. **Reminders**: Add reminders for tasks with due dates.
4. **Task Sorting**: Allow users to sort tasks by priority, due date, or category.
5. **Cloud Integration**: Save tasks to cloud storage for accessibility across devices.

---

## **8. Conclusion**
The **Advanced To-Do List Application** is a robust and user-friendly tool for managing tasks. It demonstrates the use of object-oriented programming, file handling, and user interaction in Python. With its advanced features and extensible design, it serves as a solid foundation for further development.

---

**Author**: Nathishwar  
**Date**: [19-02-2025]  
**Version**: 1.0
