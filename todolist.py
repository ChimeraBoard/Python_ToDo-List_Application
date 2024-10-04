import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    #INITialization method
    def __init__(self, root):
        self.root = root                           #Initializes the main window.
        self.root.title("Today's To Do list")      #Sets the window title.
        self.root.geometry("400x400")              #Defines the size of the window.
        self.root.configure(bg='lightblue')        #Sets the background color to light blue.
        
        self.tasks = []                            #Initializes an empty list to hold tasks.
        
        # The ToDo pop-up window Frame
        self.title_frame = tk.Frame(root, bg='lightblue')
        self.title_frame.pack(pady=10)
        self.title_label = tk.Label(self.title_frame, text="My To Do List", font=("Helvetica", 16), bg='lightblue')
        self.title_label.pack()

        self.task_entry = tk.Entry(root, width=75, bg='white', fg='black', font=("Helvetica", 12))
        self.task_entry.pack(pady=10)
        
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task, bg='#008B8B', fg='white', font=("Helvetica", 12))
        self.add_task_button.pack(pady=5)
        
        self.task_listbox = tk.Listbox(root, width=150, font=("Helvetica", 12))
        self.task_listbox.pack(pady=10)
        
        self.remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg='#B22222', fg='white', font=("Helvetica", 12))
        self.remove_task_button.pack(pady=5)

## Pop up warning for when no task was written in the task box, yet the user clicks on "Add task"
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

## Pop up warning for when no task was selected, yet the user clicks on "Remove task"
    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

#This loop ensures the application runs only when executed directly.
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()