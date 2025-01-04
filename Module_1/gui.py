from functions import file_operation
import FreeSimpleGUI
data = FreeSimpleGUI.InputText(key='-INPUT-')
to_do_window = FreeSimpleGUI.Window('To-Do App', layout=[[FreeSimpleGUI.Text("Enter your to-do")],
                                                         [data, FreeSimpleGUI.Button('Add'), FreeSimpleGUI.Button('Show')],
                                                         ])

while True:
    event, values = to_do_window.read()
    if event == FreeSimpleGUI.WINDOW_CLOSED:
        break
    if event == 'Add':
        # Add a new todo item to the list
        to_do = values['-INPUT-'] + "\n"
        # Open the file in read mode to read the current todos
        todos = file_operation('todos.txt', 'r')
        # Append the new todo item to the list
        todos.append(to_do)
        # Open the file in write mode to add new todos
        file_operation('todos.txt', 'w', todos)
        # Output a message to the window
        FreeSimpleGUI.popup(f"Task {to_do} added")
    if event == 'Show':
        todos = file_operation('todos.txt', 'r')
        if not todos:
            FreeSimpleGUI.popup("No current tasks assigned.")
        # Display all the todo items with their corresponding numbers
        else:
            formatted = "\n".join([f"{number}. {todo.capitalize()}" for number, todo in enumerate(todos, start=1)])
            window_layout = [
                [FreeSimpleGUI.Text(formatted, size=(40, len(todos) + len(todos)))],
                [FreeSimpleGUI.Button('Exit')]]
            show_window = FreeSimpleGUI.Window('Tasks', window_layout)
            while True:
                event, values = show_window.read()
                if event == FreeSimpleGUI.WINDOW_CLOSED or event == 'Exit':
                    break
            show_window.close()
    to_do_window.close()
