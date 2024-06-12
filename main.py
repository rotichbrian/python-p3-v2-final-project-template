from tabulate import tabulate
from lib.models.user import User
from lib.models.category import Category
from lib.models.task import Task
from colorama import init, Fore, Style

def main():
    init(autoreset=True)  # Initialize colorama

    while True:
        print("Task Management System")
        print("1. Create User")
        print("2. Delete User")
        print("3. Display All Users")
        print("4. Find User by ID")
        print("5. Create Category")
        print("6. Delete Category")
        print("7. Display All Categories")
        print("8. Find Category by ID")
        print("9. Create Task")
        print("10. Delete Task")
        print("11. Display All Tasks")
        print("12. Find Task by ID")
        print("13. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            user = User(id=None, name=name, email=email)
            user.save()
            print(Fore.GREEN + "User created successfully.")
        elif choice == '2':
            user_id = input("Enter user ID to delete: ")
            user = User.delete(user_id)
            if user:
              print(Fore.GREEN + "User deleted successfully.")
            else:
                print(Fore.RED + "User not found.")  
        elif choice == '3':
            users = User.get_all()
            print(tabulate(users, headers=["ID", "Name", "Email"]))
        elif choice == '4':
            user_id = input("Enter user ID to find: ")
            user = User.find_by_id(user_id)
            if user:
                print(tabulate([user], headers=["ID", "Name", "Email"]))
            else:
                print(Fore.RED + "User not found.")
        elif choice == '5':
            name = input("Enter category name: ")
            description = input("Enter category description: ")
            category = Category(id=None, name=name, description=description)
            category.save()
            print(Fore.GREEN + "Category created successfully.")
        elif choice == '6':
            category_id = input("Enter category ID to delete: ")
            category = Category.delete(category_id) 
            if category:
                print(Fore.GREEN + "Category deleted successfully.")
            else:
                print(Fore.RED + "User not found.")     
        elif choice == '7':
            categories = Category.get_all()
            print(tabulate(categories, headers=["ID", "Name", "Description"]))
        elif choice == '8':
            category_id = input("Enter category ID to find: ")
            category = Category.find_by_id(category_id)
            if category:
                print(tabulate([category], headers=["ID", "Name", "Description"]))
            else:
                print(Fore.RED + "Category not found.")
        elif choice == '9':
            user_id = input("Enter user ID: ")
            category_id = input("Enter category ID: ")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            status = input("Enter status: ")
            task = Task(id=None, user_id=user_id, category_id=category_id, title=title, description=description, due_date=due_date, status=status)
            task.save()
            print(Fore.GREEN + "Task created successfully.")
        elif choice == '10':
            task_id = input("Enter task ID to delete: ")
            Task.delete(task_id)
            print(Fore.GREEN + "Task deleted successfully.")
        elif choice == '11':
            tasks = Task.get_all()
            print(tabulate(tasks, headers=["ID", "User ID", "Category ID", "Title", "Description", "Due Date", "Status"]))
        elif choice == '12':
            task_id = input("Enter task ID to find: ")
            task = Task.find_by_id(task_id)
            if task:
                print(tabulate([task], headers=["ID", "User ID", "Category ID", "Title", "Description", "Due Date", "Status"]))
            else:
                print(Fore.RED + "Task not found.")
        elif choice == '13':
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
