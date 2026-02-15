# Simple Console To-Do List App
# Stores tasks in a text file so they remain saved

FILE_NAME = "tasks.txt"


# Load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        # file will be created automatically later
        pass
    return tasks


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


# Show all tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.\n")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
        print()


# Main program
tasks = load_tasks()

while True:
    print("====== TO DO LIST ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks(tasks)

    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task added.\n")

    elif choice == "3":
        show_tasks(tasks)
        try:
            num = int(input("Enter task number to remove: "))
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}\n")
        except:
            print("Invalid number.\n")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.\n")
