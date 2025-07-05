import os

FILENAME = "tasks.txt"

# Load existing tasks from file
def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

# Save current tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

# Display menu
def show_menu():
    print("\nTo-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Main program
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == "2":
            task = input("Enter a new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added.")
            else:
                print("Empty task not added.")
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue
            try:
                index = int(input("Enter the task number to remove: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
