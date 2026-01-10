# Student Task Manager Application
# Agile Lab Experiment 1

tasks = []

def show_menu():
    print("\n===== Student Task Manager =====")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Exit")

def add_task():
    task_name = input("Enter task name: ")
    tasks.append({"task": task_name, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} - {status}")

def complete_task():
    view_tasks()
    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
