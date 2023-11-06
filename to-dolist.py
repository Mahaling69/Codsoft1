# Empty task
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def complete_task(task_number):
    if 1 <= task_number <= len(tasks):
        completed_task = tasks.pop(task_number - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task number.")

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Complete a task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_number = int(input("Enter the task number to mark as completed: "))
        complete_task(task_number)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4).")

print("Thank you for using the to-do list application!")