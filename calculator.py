import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
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
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    label_result.config(text="Result: " + str(result))

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create input fields
entry_num1 = tk.Entry(window)
entry_num1.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create operation selection
operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar(window)
operation_var.set("+")
operation_menu = tk.OptionMenu(window, operation_var, *operations)
operation_menu.pack()

# Create Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create result label
label_result = tk.Label(window, text="Result: ")
label_result.pack()

# Run the GUI
window.mainloop()
