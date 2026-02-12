# Simple To-Do List project in Python


from unicodedata import category


todos = [] # List to store tasks

while True: # Main loop to run the program until the user decides to exit

    print("\nPlease select an option:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")
    
    # Handle user choices
    if choice == "1":
        # Add a task
        try: 
            task = input("Enter task: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time : ")
            location = input("Enter location (optional): ")
            todos.append({'task': task,
                         'date': date,
                         'time': time,
                         'location': location})
            
            print("Task added successfully!")
        except ValueError:
            print("Invalid input. Please try again.")
            continue
    
    elif choice == "2":
         # View all tasks
        if todos:
            print("\n All Tasks:")
            for i, todo in enumerate(todos, 1):
                print(f"{i} Task NO. {i}\nTask:{'-'*10}{todo['task']:10}\nDate:{'-'*10}{todo['date'] :10}\nTime:{'-'*10}{todo['time']:10}\nLocation:{'-'*10}{todo['location']:10}\n")
        else:
            print("No tasks recorded yet.")
    
    elif choice == "3":
        # Remove a task
        if todos:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(todos):
                removed = todos.pop(task_num - 1)
                print(f"Removed: {removed}")
        else:
            # If there are no tasks to remove, inform the user
            print("No tasks to remove!")
    
    elif choice == "4":
        # Exit the program
        print("Goodbye!")
        break