# Import necessary modules
import functions
import FreeSimpleGUI as sg

# Get the main application window
main_window = functions.get_main_window()

# Main event loop
while True:
    # Read events and values from the window with a timeout of 200ms
    event, values = main_window.read(timeout=200)

    # Exit the loop if the user closes the window or clicks "Exit"
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    # Update the clock display if the main window is active
    if main_window:
        try:
            # Update the clock with the current time
            current_time = functions.update_time()
            main_window["-CLOCK-"].update(value=current_time)
        except KeyError:
            # Handle error if the "-CLOCK-" key is missing
            sg.popup_error("KeyError: Unable to update the clock.")
            break

    # Handle "Add" event to add a new task
    if event == "Add":
        # Get the new task input from the user
        new_todo = values["-INPUT-"] + "\n"

        # Read existing tasks from the file
        todos = functions.file_operation("todos.txt", "r")

        # Add the new task to the list
        todos.append(new_todo)

        # Save the updated task list back to the file
        functions.file_operation("todos.txt", "w", todos)

        # Notify the user that the task has been added
        sg.popup(f"Task {new_todo} added")

    # Handle "Show" event to display all tasks
    elif event == "Show":
        # Close the main window to open the task display window
        main_window.close()

        # Read tasks from the file
        todos_list = functions.file_operation("todos.txt", "r")

        if not todos_list:
            # Notify the user if there are no tasks
            sg.popup("No current tasks assigned.")
        else:
            # Format tasks with numbering
            formatted_todos = "\n".join(
                [f"{number}. {todo.capitalize()}" for number, todo in enumerate(todos_list, start=1)]
            )
            # Define layout for the task display window
            show_window_layout = [
                [sg.Text(formatted_todos, size=(40, len(todos_list) + len(todos_list)))],
                [sg.Button("Exit")],
            ]
            # Display the tasks in a new window
            show_window = sg.Window("Tasks", show_window_layout)
            functions.close_window(show_window)
        # Reopen the main window
        main_window = functions.get_main_window()

    # Handle "Edit" event to edit a task
    elif event == "Edit":
        main_window.close()  # Close the main window

        # Read existing tasks from the file
        todos = functions.file_operation("todos.txt", "r")
        tasks_list = functions.create_list(todos)

        # Define layout for the edit task window
        edit_window_layout = [
            [
                sg.Listbox(
                    tasks_list,
                    size=(40, len(todos) + len(todos)),
                    select_mode="LISTBOX_SELECT_MODE_SINGLE",
                    enable_events=True,
                    key="-LISTBOX-",
                )
            ],
            [sg.Button("Edit"), sg.Button("Exit")],
        ]
        edit_window = sg.Window("Tasks", edit_window_layout)

        while True:
            event, values = edit_window.read()
            if event in (sg.WINDOW_CLOSED, "Exit"):
                break
            if values["-LISTBOX-"]:
                selected_task = values["-LISTBOX-"][0]
                if event == "Edit":
                    # Get the new task input from the user
                    edit_task_input = sg.InputText(key="-INPUT-", default_text=selected_task)
                    edit_task_window = sg.Window(
                        "Editing task",
                        layout=[
                            [sg.Text("Enter a new task")],
                            [edit_task_input, sg.Button("Add")],
                        ],
                    )
                    while True:
                        event, values = edit_task_window.read()
                        if event == "Add":
                            # Update the selected task in the task list
                            edit_task_input = values["-INPUT-"] + "\n"
                            task_index = todos.index(selected_task)
                            todos[task_index] = edit_task_input
                            functions.file_operation("todos.txt", "w", todos)
                            edit_window["-LISTBOX-"].update(values=todos)
                            edit_task_window.close()
                        elif event == sg.WINDOW_CLOSED:
                            break
            else:
                # Notify the user if no task is selected
                sg.popup("Task not selected. Please select a task")
        edit_window.close()
        main_window = functions.get_main_window()

    # Handle "Complete" event to mark a task as completed
    elif event == "Complete":
        main_window.close()

        # Read tasks from the file
        todos_data = functions.file_operation("todos.txt", "r")
        task_list = functions.create_list(todos_data)

        # Define layout for the complete task window
        complete_window_layout = [
            [
                sg.Listbox(
                    task_list,
                    size=(40, len(todos_data) + len(todos_data)),
                    select_mode="LISTBOX_SELECT_MODE_SINGLE",
                    enable_events=True,
                    key="-LISTBOX-",
                )
            ],
            [sg.Button("Complete"), sg.Button("Exit")],
        ]
        complete_window = sg.Window("Tasks", complete_window_layout)

        while True:
            event, values = complete_window.read()
            if event in (sg.WINDOW_CLOSED, "Exit"):
                break
            if values["-LISTBOX-"]:
                if event == "Complete":
                    selected_task = values["-LISTBOX-"][0]
                    task_index = todos_data.index(selected_task)
                    sg.popup(f"Task {selected_task} completed")
                    task_list.pop(task_index)  # Remove the completed task from the list
                    todos_data.pop(task_index)
                    functions.file_operation("todos.txt", "w", todos_data)
                    complete_window["-LISTBOX-"].update(values=todos_data)
                elif event == sg.WINDOW_CLOSED or event == "Exit":
                    break
            else:
                sg.popup("Task not selected. Please select a task")
        complete_window.close()
        main_window = functions.get_main_window()

# Close the main application window when exiting
main_window.close()
