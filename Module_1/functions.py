import time
import FreeSimpleGUI as sg


def file_operation(file, operation, data=None):
    """
    Perform file operations based on the specified mode.

    Parameters:
      file (str): The name of the file to operate on.
      operation (str): The mode of operation ('r' for read or 'w' for write).
      data (list, optional): The data to write to the file. Defaults to None.
    Returns:
      list: The data read from the file, if operation is 'r'.
    Raises:
      ValueError: If operation is not 'r' or 'w'.
    """
    try:
        with open(file, operation) as f:
            if operation == 'r':
                return f.readlines()
            elif operation == 'w':
                f.writelines(data)
    except ValueError:
        print(f"Unsupported operation. Use 'r' for read or 'w' for write.")
    except FileNotFoundError:
        print(f"Error: File not found")
    except Exception as e:
        print(f"An error occurred: {e}")


def close_window(window):
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
    window.close()


def create_list(data):
    new_list = []
    for item in data:
        new_list.append(item)
    return new_list


def update_time():
    return time.strftime('%b %d, %Y %H:%M:%S')


def get_main_window():
    layout = [
        [sg.Text("", key="-CLOCK-")],
        [sg.Text('Enter your to-do')],
        [sg.InputText(key="-INPUT-", do_not_clear=False), sg.Button('Add'), sg.Button('Show'), sg.Button('Edit'),
         sg.Button('Complete'), sg.Button('Exit')],
    ]
    return sg.Window("To-Do App", layout)
