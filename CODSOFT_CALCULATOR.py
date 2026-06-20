from tkinter import *

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operator.get()

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                result = "Cannot divide by zero"
            else:
                result = a / b
        else:
            result = "Select an operator"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Enter valid numbers")

root = Tk()
root.title("Simple Calculator")
root.geometry("350x300")

Label(root, text="CALCULATOR", font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Enter First Number").pack()
entry1 = Entry(root)
entry1.pack(pady=5)

Label(root, text="Enter Second Number").pack()
entry2 = Entry(root)
entry2.pack(pady=5)

Label(root, text="Select Operation").pack()

operator = StringVar()
operator.set("+")

OptionMenu(root, operator, "+", "-", "*", "/").pack(pady=5)

Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = Label(root, text="Result:", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
