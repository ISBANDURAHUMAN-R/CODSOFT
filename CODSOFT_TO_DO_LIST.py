from tkinter import *
from tkinter import messagebox

def add_task():
    task = task_entry.get()

    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Enter a task")

def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task")

def complete_task():
    try:
        selected = task_listbox.curselection()
        task = task_listbox.get(selected)

        if not task.startswith("✔ "):
            task_listbox.delete(selected)
            task_listbox.insert(selected, "✔ " + task)

        save_tasks()

    except:
        messagebox.showwarning("Warning", "Select a task")

def clear_tasks():
    task_listbox.delete(0, END)
    save_tasks()

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_listbox.get(0, END)

        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:

            for task in file.readlines():
                task_listbox.insert(END, task.strip())

    except:
        pass

root = Tk()
root.title("To-Do List - Itzu")
root.geometry("500x500")
root.resizable(False, False)

Label(root,
      text="TO-DO LIST",
      font=("Arial", 20, "bold")).pack(pady=10)

task_entry = Entry(root,
                   width=35,
                   font=("Arial", 12))
task_entry.pack(pady=10)

Button(root,
       text="Add Task",
       command=add_task).pack(pady=5)

frame = Frame(root)
frame.pack(pady=10)

scrollbar = Scrollbar(frame)

task_listbox = Listbox(
    frame,
    width=50,
    height=12,
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
task_listbox.pack()

Button(root,
       text="Mark Completed",
       command=complete_task).pack(pady=5)

Button(root,
       text="Delete Task",
       command=delete_task).pack(pady=5)

Button(root,
       text="Clear All",
       command=clear_tasks).pack(pady=5)

Label(root,
      text="Created by RAHUMAN",
      font=("Arial", 10)).pack(side=BOTTOM, pady=10)

load_tasks()

root.mainloop()
