import tkinter as tk

# Function to update the expression in the input field
def press(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

# Function to evaluate the final expression
def equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Calculator")

# Create input field
entry = tk.Entry(root, width=20, font=('Arial', 18), bd=10, insertwidth=2, borderwidth=4, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        action = equal
    elif text == 'C':
        action = clear
    else:
        action = lambda x=text: press(x)

    tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row, column=col, columnspan=1)
    
root.mainloop()
