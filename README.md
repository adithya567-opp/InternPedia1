Here's a general description of the code and the functions used:

1. **Importing Libraries**: The code starts by importing the required libraries, including `tkinter` and `os`.

2. **Creating the Root Window**: The `Tk()` object is created, which represents the main window of the application. The window's title, geometry, and resizability are set using the respective methods.

3. **Global Variables**: A global list `task_list` is initialized to store the tasks.

4. **addTask() Function**: This function is responsible for adding a new task to the list. It retrieves the task from the entry field, writes it to a file named "tasklist.txt", appends it to the `task_list`, and inserts it into the listbox widget.

5. **deleteTask() Function**: This function deletes a selected task from the list. It gets the selected task from the listbox, removes it from the `task_list`, updates the "tasklist.txt" file with the remaining tasks, and deletes the selected item from the listbox.

6. **openTaskFile() Function**: This function reads the tasks from the "tasklist.txt" file and populates the `task_list` and the listbox widget. If the file doesn't exist, it creates a new empty file.

7. **GUI Elements**:
   - **Top Bar**: The top bar displays the application title and icons.
   - **Entry Field**: An entry field is provided for users to input new tasks.
   - **Add Button**: A button is created to trigger the `addTask()` function when clicked.
   - **Listbox**: A listbox widget is used to display the tasks. It is placed inside a frame with a scrollbar.
   - **Delete Button**: A button with a delete icon is created to trigger the `deleteTask()` function when clicked.

8. **Initialization**: The `openTaskFile()` function is called to populate the listbox with existing tasks from the file.

9. **Main Loop**: The `root.mainloop()` method is called at the end to start the main event loop and display the GUI application.

The code utilizes various Tkinter widgets, such as labels, buttons, frames, and listboxes, to create the user interface. It also incorporates image handling using the `PhotoImage` class from Tkinter.

The main functions, `addTask()`, `deleteTask()`, and `openTaskFile()`, handle the core functionality of adding, deleting, and loading tasks, respectively. These functions interact with the GUI elements and the "tasklist.txt" file to persist and manage the tasks.

Overall, this Python script creates a simple To-Do List application with a graphical user interface, allowing users to add, delete, and view tasks conveniently.
