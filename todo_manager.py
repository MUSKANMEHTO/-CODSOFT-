"""
todo_manager.py

A professional Command-Line To-Do List application in Python.
Uses `rich` for styled output and `inquirer` for interactive menus.
"""

import os
import json
import inquirer
from rich.console import Console
from rich.table import Table

# File where tasks are stored
TASKS_FILE = "tasks.json"

# Console object for rich output
console = Console()


def load_tasks():
    """
    Load tasks from the JSON file.
    Returns a list of task dictionaries.
    """
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    """
    Save the list of tasks to the JSON file.
    """
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    """
    Display tasks in a styled table.
    """
    if not tasks:
        console.print("\n[bold red]📭 No tasks found.[/bold red]")
        return

    table = Table(title="📋 To-Do List", show_lines=True)
    table.add_column("No.", justify="right", style="cyan", width=4)
    table.add_column("Task", style="magenta")
    table.add_column("Status", style="green")

    for index, task in enumerate(tasks, start=1):
        status = "✅ Done" if task["done"] else "❌ Not Done"
        table.add_row(str(index), task["task"], status)

    console.print(table)


def add_task(tasks):
    """
    Prompt user to add a new task.
    """
    task_text = input("📝 Enter new task: ").strip()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        console.print("[green]🟢 Task added successfully.[/green]")
    else:
        console.print("[yellow]⚠️ Task cannot be empty![/yellow]")


def mark_done(tasks):
    """
    Allow user to select one or more tasks to mark as done.
    """
    if not tasks:
        console.print("[red]❌ No tasks available to mark.[/red]")
        return

    choices = [f"{i + 1}. {t['task']}" for i, t in enumerate(tasks)]
    question = [
        inquirer.Checkbox("done_tasks", message="Select tasks to mark as done", choices=choices)
    ]
    answer = inquirer.prompt(question)

    if answer and "done_tasks" in answer:
        for selected in answer["done_tasks"]:
            idx = int(selected.split(".")[0]) - 1
            tasks[idx]["done"] = True
        console.print("[green]✅ Selected tasks marked as done.[/green]")


def delete_task(tasks):
    """
    Allow user to delete a task from the list.
    """
    if not tasks:
        console.print("[red]❌ No tasks to delete.[/red]")
        return

    choices = [f"{i + 1}. {t['task']}" for i, t in enumerate(tasks)]
    question = [
        inquirer.List("task_to_delete", message="Select a task to delete", choices=choices)
    ]
    answer = inquirer.prompt(question)

    if answer and "task_to_delete" in answer:
        idx = int(answer["task_to_delete"].split(".")[0]) - 1
        removed = tasks.pop(idx)
        console.print(f"[yellow]🗑️ Task '{removed['task']}' deleted.[/yellow]")


def main_menu():
    """
    Display the main menu and return the selected option.
    """
    question = [
        inquirer.List(
            "choice",
            message="What would you like to do?",
            choices=[
                "View Tasks",
                "Add Task",
                "Mark Task as Done",
                "Delete Task",
                "Exit"
            ],
        )
    ]
    answer = inquirer.prompt(question)
    return answer["choice"] if answer else "Exit"


def main():
    """
    Main function to run the To-Do List manager.
    """
    tasks = load_tasks()
    console.print("\n[bold cyan]📌 Welcome to To-Do Manager[/bold cyan]")

    while True:
        choice = main_menu()

        if choice == "View Tasks":
            display_tasks(tasks)
        elif choice == "Add Task":
            add_task(tasks)
        elif choice == "Mark Task as Done":
            mark_done(tasks)
        elif choice == "Delete Task":
            delete_task(tasks)
        elif choice == "Exit":
            save_tasks(tasks)
            console.print("[bold green]💾 Tasks saved. Goodbye![/bold green]")
            break


if __name__ == "__main__":
    main()
