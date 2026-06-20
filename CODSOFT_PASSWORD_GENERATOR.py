# Import required libraries
# Functions
# Main Window
# Buttons and Widgets
# Start Application
from tkinter import *
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        chars = ""

        if upper_var.get():
            chars += string.ascii_uppercase

        if lower_var.get():
            chars += string.ascii_lowercase

        if digit_var.get():
            chars += string.digits

        if symbol_var.get():
            chars += string.punctuation

        if chars == "":
            messagebox.showwarning("Warning", "Select at least one option")
            return

        password = ''.join(random.choice(chars) for _ in range(length))

        password_entry.delete(0, END)
        password_entry.insert(0, password)

        if length < 8:
            strength_label.config(text="Weak")
        elif length < 12:
            strength_label.config(text="Medium")
        else:
            strength_label.config(text="Strong")

    except:
        messagebox.showerror("Error", "Enter a valid length")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard")

root = Tk()
root.title("Password Generator - RAHUMAN")
root.geometry("450x400")
root.resizable(False, False)

Label(root, text="Password Generator",
      font=("Arial", 18, "bold")).pack(pady=10)

Label(root, text="Password Length").pack()

length_entry = Entry(root)
length_entry.pack(pady=5)

upper_var = IntVar(value=1)
lower_var = IntVar(value=1)
digit_var = IntVar(value=1)
symbol_var = IntVar(value=1)

Checkbutton(root, text="Uppercase Letters",
            variable=upper_var).pack()

Checkbutton(root, text="Lowercase Letters",
            variable=lower_var).pack()

Checkbutton(root, text="Numbers",
            variable=digit_var).pack()

Checkbutton(root, text="Symbols",
            variable=symbol_var).pack()

Button(root, text="Generate Password",
       command=generate_password).pack(pady=10)

password_entry = Entry(root,
                       width=35,
                       font=("Arial", 12))
password_entry.pack(pady=10)

Button(root, text="Copy Password",
       command=copy_password).pack()

strength_label = Label(root,
                       text="Strength",
                       font=("Arial", 12))
strength_label.pack(pady=10)

Label(root,
      text="Created by RAHUMAN",
      font=("Arial", 10)).pack(side="bottom", pady=10)

root.mainloop()
