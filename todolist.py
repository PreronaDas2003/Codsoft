import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        # Create GUI elements
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add task", command=self.add_task)
        self.add_button.pack()

        self.task_list = tk.Listbox(root, width=40)
        self.task_list.pack()

        self.delete_button = tk.Button(root, text="Delete task", command=self.delete_task)
        self.delete_button.pack()

        self.complete_button = tk.Button(root, text="Mark as completed", command=self.complete_task)
        self.complete_button.pack()

        self.clear_button = tk.Button(root, text="Clear all tasks", command=self.clear_tasks)
        self.clear_button.pack()

        self.save_button = tk.Button(root, text="Save tasks", command=self.save_tasks)
        self.save_button.pack()

        self.load_button = tk.Button(root, text="Load tasks", command=self.load_tasks)
        self.load_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except:
            messagebox.showerror("Error", "Select a task to delete")

    def complete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.task_list.get(task_index)
            self.task_list.delete(task_index)
            self.task_list.insert(task_index, task + " (Completed)")
            self.tasks[task_index] += " (Completed)"
        except:
            messagebox.showerror("Error", "Select a task to mark as completed")

    def clear_tasks(self):
        self.task_list.delete(0, tk.END)
        self.tasks = []

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.tasks = [line.strip() for line in f]
            self.task_list.delete(0, tk.END)
            for task in self.tasks:
                self.task_list.insert(tk.END, task)
        except FileNotFoundError:
            messagebox.showerror("Error", "No saved tasks found")

root = tk.Tk()
todo_list = ToDoList(root)
root.mainloop()