tasks = []

def show_tasks():
    if not tasks:
        print("There are no tasks yet.")
    else:
        for i,task in enumerate(tasks):
            if task["done"] == True:
                status = "✅"
            else:
                status = "❌"
            print(f"{1+i}. {task["task"]} [{status}]")

def add_task():
    task = input("Enter your task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")


def mark_done():
    show_tasks()
    i = int(input("Enter the task you want to mark as done: ")) - 1
    if 0 <= i < len(tasks):
        tasks[i]["done"] = True
        print("Task marked as done!")

def delete_task():
    show_tasks()
    i = int(input("Enter task you wish to remove: ")) - 1
    if 0 <= i < len(tasks):
        tasks.pop(i)
        print("Task removed succesfully!")


while True:
    print("\n1. Add task\n2. Show tasks\n3. Mark Done\n4. Delete task\n5. Exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        show_tasks()
    elif choice == 3:
        mark_done()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid number")
        continue