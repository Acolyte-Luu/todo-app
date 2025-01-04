from functions import file_operation
import time

# Start an infinite loop to keep the program running until the user chooses to exit

current_time = time.strftime('Date: %b %d,%Y \nTime: %H:%M:%S')
print(current_time)
while True:
    # Prompt the user to choose an action and convert the input to lowercase
    user_choice = input("Type Add, Show, Edit, Complete or Exit: ").lower()
    # Check the user's choice with the corresponding action
    if 'add' in user_choice[0:3]:
        # Add a new todo item to the list
        to_do = user_choice[4:] + "\n"  # Append newline character
        # Open the file in read mode to read the current todos
        todos = file_operation('todos.txt', 'r')
        # Append the new todo item to the list
        todos.append(to_do)
        # Open the file in write mode to add new todos
        file_operation('todos.txt', 'w', todos)

    elif 'show' in user_choice[0:4]:
        # Open the file in read mode to read the current todos
        todos = file_operation('todos.txt', 'r')
        if not todos:
            print("No current tasks assigned.")
        # Display all the todo items with their corresponding numbers
        else:
            for number, todo in enumerate(todos, start=1):
                todo = todo.strip('\n')
                print(f"{number}. {todo.capitalize()}")

    elif 'edit' in user_choice[0:4]:
        # Edit an existing todo item
        try:
            todos = file_operation('todos.txt', 'r')
            edit_task = int(user_choice[5:])  # Get the task number to edit
            edit_task = edit_task - 1  # Convert to zero-based index
            stripped = todos[edit_task].strip('\n')
            print(f"Editing task {stripped}")
            new_todo = input("Enter a new task: ") + "\n"  # Get the new task description
            todos[edit_task] = new_todo  # Replace the old task with the new one
            # Open the file in write mode to replace todo with the new todo
            file_operation('todos.txt', 'w', todos)
        except ValueError:
            print("Invalid command. Please enter the number of the task you want to edit after typing 'edit'.")

    elif 'complete' in user_choice[0:8]:
        # Mark a task as complete and remove it from the list
        try:
            todos = file_operation('todos.txt', 'r')
            complete_task = int(user_choice[9:])  # Get the task number to complete
            complete_task = complete_task - 1  # Convert to zero-based index
            stripped = todos[complete_task].strip('\n')
            print(f"Task {stripped} completed")  # Print a confirmation message
            todos.pop(complete_task)  # Remove the completed task from the list
            # Open the file in write mode to remove the completed todo
            file_operation('todos.txt', 'w', todos)
        except ValueError:
            print("Invalid command. Please enter the number of the task you want to complete after typing 'complete'.")
        except IndexError:
            print("Invalid task. Please enter a valid number of the task you want to complete after typing 'complete'.")
    elif 'exit' in user_choice[0:4]:
        print("Thanks")
        break  # Break the loop to end the program

    else:
        print("Command is not valid.")
