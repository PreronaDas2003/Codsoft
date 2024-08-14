from tkinter import *

window = Tk()
window.title("Simple Calculator")

num1_label = Label(window, text="Number 1:")
num1_label.grid(row=0, column=0)
num1_entry = Entry(window)
num1_entry.grid(row=0, column=1)

num2_label = Label(window, text="Number 2:")
num2_label.grid(row=1, column=0)
num2_entry = Entry(window)
num2_entry.grid(row=1, column=1)

operation_label = Label(window, text="Operation:")
operation_label.grid(row=2, column=0)
operation_var = StringVar()
operation_var.set("+")
operation_menu = OptionMenu(window, operation_var, "+", "-", "*", "/", "%")
operation_menu.grid(row=2, column=1)

result_label = Label(window, text="Result:")
result_label.grid(row=3, column=0)
result_entry = Entry(window)
result_entry.grid(row=3, column=1)

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operation = operation_var.get()
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero is not allowed"
        elif operation == "%":
            if num2 != 0:
                result = num1 % num2
            else:
                result = "Error: Division by zero is not allowed"
        result_entry.delete(0, END)
        result_entry.insert(0, result)
    except ValueError:
        result_entry.delete(0, END)
        result_entry.insert(0, "Error: Invalid input")

calculate_button = Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=0, columnspan=2)
window.mainloop()