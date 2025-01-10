# Todo List Manager

This project is a simple **Todo List Manager** application built with Python using the **FreeSimpleGUI** library for the graphical user interface (GUI). The application allows users to manage their tasks by adding, displaying, editing, and marking them as complete.

## Features

- **Add New Task**: Add a new todo task to your list.
- **Show Tasks**: Display all tasks currently in the list.
- **Edit Task**: Edit an existing task from the list.
- **Complete Task**: Mark a task as completed and remove it from the list.
- **Real-Time Clock**: A clock displayed in the main window.
- **Error Handling**: Informative error messages for potential issues.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repository/todo-list-manager.git
   cd todo-list-manager
   ```

2. **Install Required Dependencies**
   Ensure you have Python 3.x installed on your machine. Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Execute the main Python script to launch the application:
   ```bash
   python main.py
   ```

## File Structure

- **main.py**: Entry point of the application, handles the GUI and logic.
- **functions.py**: Contains helper functions for file operations, task management, and GUI setup.
- **todos.txt**: Stores the list of tasks persistently.

## Usage

1. **Adding a Task**:
   - Enter the task in the input box.
   - Click the "Add" button.

2. **Displaying Tasks**:
   - Click the "Show" button to view all current tasks in a new window.

3. **Editing a Task**:
   - Click the "Edit" button.
   - Select a task from the list and provide the new task details.

4. **Completing a Task**:
   - Click the "Complete" button.
   - Select the task you wish to mark as complete.

5. **Exit**:
   - Close any window or click the "Exit" button to quit the application.

## Error Handling

- If the clock cannot be updated, an error popup is displayed.
- If no task is selected during edit or completion, the application prompts the user to select a task.

## Requirements

- Python 3.7+
- FreeSimpleGUI

## Future Enhancements

- Add support for setting task deadlines.
- Enable prioritization of tasks.
- Add a search feature to quickly locate tasks.
- Support for saving tasks to a database instead of a text file.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request with your enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the developers of FreeSimpleGUI for their excellent GUI library.

