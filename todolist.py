class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the to-do list.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

# Create a TodoList instance
todo_list = TodoList()

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        new_task = input("Enter the task: ")
        todo_list.add_task(new_task)
    elif choice == "2":
        task_to_remove = input("Enter the task to remove: ")
        todo_list.remove_task(task_to_remove)
    elif choice == "3":
        todo_list.display_tasks()
    elif choice == "4":
        print("Exiting the To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
