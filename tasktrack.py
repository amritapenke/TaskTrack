
"""A command-line task manager created for CPS 310.

Author: Amrita Penke
Course: CPS 310
"""
TASKS_FILE = "tasks.txt"
def load_tasks(filename):
    """Load tasks from a text file."""
    tasks = []

    try:
        with open(filename, "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
    except FileNotFoundError:
        return []

    return tasks

def save_tasks(tasks, filename):
    """Save the current task list to a text file."""
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
        

def display_menu():
    """Display the available TaskTrack menu options."""
    print("\nTaskTrack")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")


def add_task(tasks):
    """Add a task and save it to the file."""
    task = input("Enter a new task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    tasks.append(task)

    with open(TASKS_FILE, "a") as file:
        file.write(task + "\n")

    print("Task added successfully!")


def view_tasks(tasks):
    """Display all tasks currently stored."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")


def remove_task_by_number(tasks, task_number):
    """Remove and return a task by its displayed number, or return None."""
    if task_number < 1 or task_number > len(tasks):
        return None

    return tasks.pop(task_number - 1)


def remove_task(tasks):
    """Remove a task by its number. Return True if successful."""
    if not tasks:
        print("No tasks are available to remove.")
        return False

    view_tasks(tasks)
    selection = input("Enter the number of the task to remove: ").strip()

    if not selection.isdigit():
        print("Please enter a valid task number.")
        return False

    task_number = int(selection)
    removed_task = remove_task_by_number(tasks, task_number)

    if removed_task is None:
        print("That task number does not exist.")
        return False

    print(f"Removed task: {removed_task}")
    return True


def main():
    """Run the TaskTrack menu until the user chooses to exit."""
    tasks = load_tasks(TASKS_FILE)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            if remove_task(tasks):
                save_tasks(tasks, TASKS_FILE)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
