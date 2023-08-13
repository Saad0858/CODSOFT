import os

class Task:
    def __init__(self, task_id, title, description, status="Incomplete", due_date=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(f"Task ID: {task.task_id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Status: {task.status}")
            print(f"Due Date: {task.due_date}")
            print()

    def update_task_status(self, task_id, new_status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = new_status
                break

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def save_tasks_to_file(self, filename="tasks.txt"):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.task_id};{task.title};{task.description};{task.status};{task.due_date}\n")

    def load_tasks_from_file(self, filename="tasks.txt"):
        if not os.path.exists(filename):
            return

        with open(filename, "r") as file:
            for line in file:
                task_data = line.strip().split(";")
                task_id, title, description, status, due_date = task_data
                self.tasks.append(Task(task_id, title, description, status, due_date))

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.load_tasks_from_file()

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Save and Quit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (optional): ")
            todo_list.add_task(Task(task_id, title, description, due_date=due_date))
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_id = input("Enter Task ID to update status: ")
            new_status = input("Enter New Status: ")
            todo_list.update_task_status(task_id, new_status)
        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            todo_list.delete_task(task_id)
        elif choice == "5":
            todo_list.save_tasks_to_file()
            break
        else:
            print("Invalid choice. Please try again.")
