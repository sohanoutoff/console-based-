# Create a console-based To-Do list that lets you add, view, and delete tasks using a list or file.
# using list 
console= []
 # View all tasks in the console list
def view_tasks():
   
    if not console:
        print("No tasks available.")
    else: 
        print("Tasks:")
        for i, task in enumerate(console, start=1):
            print(f"{i}. {task}")

# Add a task to the console list
def add_task():
    
    try:
        check = input("For character task press 'cha', for integer task press 'int', for float task press 'float': ")
        if check.lower() == "cha":
            task = input("Enter a character task: ")
        elif check.lower() == "int":
            task = int(input("Enter an integer task: "))
        elif check.lower() == "float":
            task = float(input("Enter a float task: "))
        else:
            print("Invalid option.")
            return
        console.append(task)
        print("Task added.")
    except ValueError:
        print("Invalid input. Please enter a valid task.")
    finally: view_tasks()

# Delete a task from the console list

def delete_task(task_number):
    view_tasks()

    try:
        task_number = int(task_number) - 1
        if 0 <= task_number < len(console):
            removed_task = console.pop(task_number)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except Exception as e:
        print(f"Error: {e}")
    finally: view_tasks()
    
print("Welcome to the To-Do List App!")
while True:
    try:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = input("Enter the task number to delete: ")
            delete_task(task_number)
        elif choice == '4':
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("thank u")

