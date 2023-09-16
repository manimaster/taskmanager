# (c) 2018 Manikandan
import json
from task import Task
from user import User

def load_data():
    try:
        with open('data/tasks.json', 'r') as task_file:
            tasks_data = json.load(task_file)
    except FileNotFoundError:
        tasks_data = []

    try:
        with open('data/users.json', 'r') as user_file:
            users_data = json.load(user_file)
    except FileNotFoundError:
        users_data = []

    return tasks_data, users_data

def save_data(tasks_data, users_data):
    with open('data/tasks.json', 'w') as task_file:
        json.dump(tasks_data, task_file, indent=4)

    with open('data/users.json', 'w') as user_file:
        json.dump(users_data, user_file, indent=4)

def main():
    tasks_data, users_data = load_data()

    while True:
        print("Task Manager Menu:")
        print("1. Login")
        print("2. Register")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            user = next((u for u in users_data if u['username'] == username and u['password'] == password), None)

            if user:
                logged_user = User(user['username'], user['password'])
                for task_data in tasks_data:
                    if task_data['user'] == username:
                        task = Task(task_data['title'], task_data['description'], task_data['completed'])
                        logged_user.add_task(task)

                while True:
                    print("User Menu:")
                    print("1. View tasks")
                    print("2. Add task")
                    print("3. Mark task as completed")
                    print("4. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        print(logged_user)

                    elif user_choice == '2':
                        title = input("Enter task title: ")
                        description = input("Enter task description: ")
                        new_task = Task(title, description)
                        logged_user.add_task(new_task)
                        tasks_data.append({'user': username, 'title': title, 'description': description, 'completed': False})
                        save_data(tasks_data, users_data)

                    elif user_choice == '3':
                        print("Your tasks:")
                        for i, task in enumerate(logged_user.tasks):
                            print(f"{i + 1}. {task.title} - {'Completed' if task.completed else 'Incomplete'}")
                        task_index = int(input("Enter the task number to mark as completed: ")) - 1
                        if 0 <= task_index < len(logged_user.tasks):
                            logged_user.tasks[task_index].mark_as_completed()
                            tasks_data[task_index]['completed'] = True
                            save_data(tasks_data, users_data)
                        else:
                            print("Invalid task number.")

                    elif user_choice == '4':
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Invalid username or password.")

        elif choice == '2':
            username = input("Enter a new username: ")
            password = input("Enter a new password: ")
            users_data.append({'username': username, 'password': password})
            save_data(tasks_data, users_data)
            print("Registration successful!")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
