 



# (link unavailable)

class TodoList:
    def __init__(self):
        self.tasks = {}

    def show_tasks(self):
        print("\nTo-Do List:")
        for id, task in self.tasks.items():
            print(f"{id}: {task['description']} ({task['status']})")

    def add_task(self):
        description = input("Enter task description: ")
        self.tasks[len(self.tasks) + 1] = {"description": description, "status": "Pending"}
        print("Task added successfully!")

    def update_task(self):
        self.show_tasks()
        task_id = int(input("Enter task ID to update: "))
        if task_id in self.tasks:
            status = input("Enter new status (Pending/Done): ")
            self.tasks[task_id]["status"] = status
            print("Task updated successfully!")
        else:
            print("Invalid task ID.")

    def delete_task(self):
        self.show_tasks()
        task_id = int(input("Enter task ID to delete: "))
        if task_id in self.tasks:
            del self.tasks[task_id]
            print("Task deleted successfully!")
        else:
            print("Invalid task ID.")


def main():
    todo = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo.show_tasks()
        elif choice == "2":
            todo.add_task()
        elif choice == "3":
            todo.update_task()
        elif choice == "4":
            todo.delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


 
