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
    """
    Close the given window when a close event or 'Exit' event occurs.

    Args:
        window (sg.Window): The PySimpleGUI window to be closed.

    Description:
        This function continuously reads events from the given window. When a close event
        (such as the window being closed) or an 'Exit' button event is detected, it breaks
        the loop and closes the window.
    """
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
    window.close()


def create_list(data):
    """
    Create a new list from the provided data.

    Args:
        data (list): The input list containing items to be added to the new list.

    Returns:
        list: A new list containing the items from the input data.
    """
    new_list = []
    for item in data:
        new_list.append(item)
    return new_list


def update_time():
    """
    Get the current date and time as a formatted string.

    Returns:
        str: The current date and time formatted as '%b %d, %Y %H:%M:%S'.
    """
    return time.strftime('%b %d, %Y %H:%M:%S')


def get_main_window():
    """
    Create and return the main window for the To-Do App.

    Returns:
        sg.Window: The main window with the clock, input field, and buttons for the To-Do App.
    """
    layout = [
        [sg.Text("", key="-CLOCK-")],
        [sg.Text('Enter your to-do')],
        [sg.InputText(key="-INPUT-", do_not_clear=False), sg.Button('Add'), sg.Button('Show'), sg.Button('Edit'),
         sg.Button('Complete'), sg.Button('Exit')],
    ]
    return sg.Window("To-Do App", layout)
