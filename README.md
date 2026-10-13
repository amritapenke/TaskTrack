
# TaskTrack

A command-line task manager developed in Python for CPS 310.

## Features

- View saved tasks
- Add new tasks
- Reject empty task input
- Save tasks permanently in `tasks.txt`
- Automatically load tasks when the program starts
- Exit through a menu

## How to Run

Open a terminal in the TaskTrack folder and run:

```bash
python3 tasktrack.py
```

## Menu Options

1. View tasks
2. Add task
3. Exit

## Persistent Storage

TaskTrack uses `tasks.txt` to store tasks. When a new task is added, it is saved to the file. Previously saved tasks are loaded when the program starts again.

## Version Control

Git and GitHub were used to track development through multiple meaningful commits.

## Author

Amrita Penke  
CPS 310
## Remove Task Feature

Users can select option 3 to remove a task by its number.

The program checks for invalid inputs, including letters,
zero, and numbers outside the task list.

After a successful removal, the updated tasks are saved
to tasks.txt so deleted tasks do not return.