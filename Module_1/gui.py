from functions import file_operation
import FreeSimpleGUI as sg

todo_input = sg.InputText(key="-INPUT-", do_not_clear=False)
main_window = sg.Window(
    "To-Do App",
    layout=[
        [sg.Text("Enter your to-do")],
        [todo_input, sg.Button("Add"), sg.Button("Show"), sg.Button("Edit"), sg.Button("Complete")],
    ],
)

while True:
    event, values = main_window.read()
    if event == "Add":
        # Add a new todo item to the list
        new_todo = values["-INPUT-"] + "\n"
        # Open the file in read mode to read the current todos
        todos = file_operation("todos.txt", "r")
        # Append the new todo item to the list
        todos.append(new_todo)
        # Open the file in write mode to add new todos
        file_operation("todos.txt", "w", todos)
        # Output a message to the window
        sg.popup(f"Task {new_todo} added")

    elif event == "Show":
        todos_list = file_operation("todos.txt", "r")
        if not todos_list:
            sg.popup("No current tasks assigned.")
        # Display all the todo items with their corresponding numbers
        else:
            formatted_todos = "\n".join(
                [
                    f"{number}. {todo.capitalize()}"
                    for number, todo in enumerate(todos_list, start=1)
                ]
            )
            show_window_layout = [
                [
                    sg.Text(
                        formatted_todos, size=(40, len(todos_list) + len(todos_list))
                    )
                ],
                [sg.Button("Exit")],
            ]
            show_window = sg.Window("Tasks", show_window_layout)
            while True:
                event, values = show_window.read()
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
            show_window.close()

    elif event == "Edit":
        todos = file_operation("todos.txt", "r")
        tasks_list = [todo for todo in todos]
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
            if event in (sg.WINDOW_CLOSED, 'Exit'):
                break
            if values["-LISTBOX-"]:
                selected_task = values["-LISTBOX-"][0]
                if event == "Edit":
                    edit_task_input = sg.InputText(key="-INPUT-")
                    edit_task_window = sg.Window(
                        "To-Do App",
                        layout=[
                            [sg.Text("Enter a new task")],
                            [edit_task_input, sg.Button("Add")],
                        ],
                    )
                    while True:
                        event, values = edit_task_window.read()
                        if event == "Add":
                            edit_task_input = values["-INPUT-"] + "\n"
                            task_index = todos.index(selected_task)
                            todos[task_index] = edit_task_input
                            file_operation("todos.txt", "w", todos)
                            edit_window['-LISTBOX-'].update(values=todos)
                            edit_task_window.close()
                        elif event == sg.WINDOW_CLOSED:
                            break
            else:
                sg.popup("Task not selected. Please select a task")
        edit_window.close()

    elif event == 'Complete':
        todos_data = file_operation("todos.txt", "r")
        task_list = [todo for todo in todos_data]
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
            if event in (sg.WINDOW_CLOSED, 'Exit'):
                break
            if values["-LISTBOX-"]:
                if event == "Complete":
                    selected_task = values["-LISTBOX-"][0]
                    task_index = todos_data.index(selected_task)
                    sg.popup(f"Task {selected_task} completed")
                    task_list.pop(task_index)
                    todos_data.pop(task_index)  # Remove the completed task from the list
                    # Open the file in write mode to remove the completed todo
                    file_operation('todos.txt', 'w', todos_data)
                    complete_window['-LISTBOX-'].update(values=todos_data)
                elif event == sg.WINDOW_CLOSED or event == "Exit":
                    break
            else:
                sg.popup("Task not selected. Please select a task")

        complete_window.close()

    elif event == sg.WINDOW_CLOSED:
        break
main_window.close()
