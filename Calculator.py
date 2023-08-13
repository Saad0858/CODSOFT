import tkinter as tk
from math import sqrt

def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

def on_clear():
    entry.delete(0, tk.END)

def on_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def on_square_root():
    try:
        value = float(entry.get())
        result = sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x460+600+180")
root.resizable(False, False)

# Create a text entry widget
entry = tk.Entry(root, font=("comic sans ms", 20), justify=tk.RIGHT)
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

# Square root button
sqrt_button = tk.Button(root, text="√", font=("comic sans ms", 16), padx=20, pady=10, command=on_square_root)
sqrt_button.grid(row=1, column=1, padx=5, pady=5)

# Special buttons
clear_button = tk.Button(root, text="C", font=("comic sans ms", 16), padx=20, pady=10, command=on_clear)
clear_button.grid(row=1, column=0, padx=5, pady=5)

equal_button = tk.Button(root, text="=", font=("comic sans ms", 16), padx=20, pady=10, command=on_equal)
equal_button.grid(row=5, column=3, padx=5, pady=5)

# Define the buttons
buttons = [
    ('/', 1, 2),('+', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('.', 4, 3),
    ('(', 5, 0), ('0', 5, 1), (')', 5, 2),
]

# Create and place the buttons on the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("comic sans ms", 16), padx=20, pady=10, command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)




# Run the main event loop
root.mainloop()
