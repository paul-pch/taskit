import typer
from rich.console import Console
from rich.table import Table
import json
import os
import time

app = typer.Typer()
console = Console()

# Function to load tasks from the configuration file
def load_tasks():
    home = os.path.expanduser("~")
    config_file = os.path.join(home, ".tasks.json")
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            return json.load(f)
    return []

# Function to save tasks to the configuration file
def save_tasks(tasks):
    home = os.path.expanduser("~")
    config_file = os.path.join(home, ".tasks.json")
    with open(config_file, "w") as f:
        json.dump(tasks, f)

# Function to display tasks
def display_tasks(tasks):
    # Count the number of tasks in each status
    todo_count = sum(1 for task in tasks if task["status"] == "TODO")
    run_count = sum(1 for task in tasks if task["status"] == "RUN")
    done_count = sum(1 for task in tasks if task["status"] == "DONE")
    review_count = sum(1 for task in tasks if task["status"] == "REVIEW")

    table = Table(title="Tasks")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column(f"TODO ({todo_count})", justify="left", style="cyan", no_wrap=True)
    table.add_column(f"RUN ({run_count})", justify="left", style="yellow")
    table.add_column(f"REVIEW ({review_count})", justify="left", style="magenta")
    table.add_column(f"DONE ({done_count})", justify="left", style="green")

    # Iterate over tasks and add a new row to the table for each task
    for task in tasks:
        if task["status"] == "TODO":
            table.add_row(str(task["id"]), task["label"], "", "", "")
        elif task["status"] == "RUN":
            table.add_row(str(task["id"]), "", task["label"], "", "")
        elif task["status"] == "REVIEW":
            table.add_row(str(task["id"]), "", "", task["label"], "")
        elif task["status"] == "DONE":
            table.add_row(str(task["id"]), "", "", "", task["label"])

    console.print(table)

# Function to add a new task
@app.command()
def add(label: str, status: str = typer.Option("TODO", help="Task status (TODO, RUN, REVIEW, DONE)")):
    tasks = load_tasks()
    id = int(time.time())
    tasks.append({"id": id, "label": label, "status": status})
    save_tasks(tasks)
    console.print(f"Task {id} created successfully.")

# Function to edit a task
@app.command()
def edit(id: int, label: str = None, status: str = None):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            if label is not None:
                task["label"] = label
            if status is not None:
                task["status"] = status
            save_tasks(tasks)
            console.print(f"Task {id} updated successfully.")
            return
    console.print(f"Task {id} not found.")

# Function to remove "done" tasks
@app.command()
def clear():
    tasks = load_tasks()
    tasks = [task for task in tasks if task["status"] != "DONE"]
    save_tasks(tasks)
    console.print("All tasks with status DONE have been removed.")

# Command to list all tasks
@app.command()
def list():
    tasks = load_tasks()
    display_tasks(tasks)


if __name__ == "__main__":
    app()
