tasks = []

def display_task(tasks=None):
    if not tasks:
        print("No Tasks is added")
    else:
        print("To-Do List:")
        for i, tasks in enumerate(tasks, start=1):
            status = "Done" if tasks ["completed"] else "Not done"
            print(f"{i}. {tasks['task']} ({status})")

def add_tasks(tasks_name):
    task = {"tasks": tasks_name, "compeleted":False}
    tasks.append(task)
    print(f"Task '{tasks_name}' added to your To-do list")

print("OPTION :")
print("1. Display the TO-Do List")
print("2. Add a Task")
print("3. Mark a Task as complete")
print("4. Remove a Task")
print("5. Quit")
choice=input("Enter a your choice :")

if choice == 1 :
    display_task()