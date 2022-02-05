import tkinter as tk
from tkinter import messagebox

MEMORY = None


# Update method to update the value of the stringvar
def update(string):
    text.set(text.get() + string)


# Functions to use the memory
def add_memory():
    """Add a value to the memory"""
    globals()["MEMORY"] = text.get()


def clear_memory():
    """Clear the value in the memory"""
    globals()["MEMORY"] = None


def recall_memory():
    """Insert the memory value in the textbox"""

    m = globals()["MEMORY"]
    update(m if m is not None else "0")


def show_history():
    """Create a toplevel window and show the text in the data text file"""
    win = tk.Toplevel()
    win.geometry("100x100")
    with open("./data.txt", "r") as file:
        file_text = "".join(file.readlines())

    label = tk.Label(win, text=file_text)
    label.pack()
    win.mainloop()


def add_to_history(operation, result):
    """Add an entry of a opertion in the data text file"""
    with open("./data.txt", "r+") as file:
        line = len(file.readlines())
        file.write(f"{line+1}) {operation} = {result}\n")


def result():
    """Evaulate the expression and show a message if there are any errors"""
    try:
        output = eval(text.get())
        add_to_history(text.get(), output)
        text.set(output)
    except NameError:
        messagebox.showwarning("Error", "Invalid syntax")
    except ZeroDivisionError:
        messagebox.showwarning("Error", "Could not divide by zero")
    except SyntaxError:
        messagebox.showwarning("Error", "Invalid syntax")


# Create an instance of a new GUI window
root = tk.Tk()
root.geometry("200x175")
root.title("Calculator")

# GUI component that contains all buttons on the left
menu = tk.Frame(root)
menu.pack(side=tk.LEFT)

# Creating a textvarible to store the text of the calculator
text = tk.StringVar()

# Creating buttons on the menu component
btn1 = tk.Button(menu, text="History", height=2, width=5, command=show_history)
btn2 = tk.Button(menu, text="M+", height=2, width=5, command=add_memory)
btn3 = tk.Button(menu, text="M-", height=2, width=5, command=clear_memory)
btn4 = tk.Button(menu, text="MRC", height=2, width=5, command=recall_memory)

# Displaying the buttons on the window using the grid geometry manager
btn1.grid(row=0)
btn2.grid(row=1)
btn3.grid(row=2)
btn4.grid(row=3)


textarea = tk.Label(root, textvariable=text, bg="white")
textarea.pack(fill="both", expand=True)

button_frame = tk.Frame(root)
button_frame.pack()


# Creating all the buttons for numbers and utility
button1 = tk.Button(button_frame, text="1", command=lambda: update("1"), padx=10)
button2 = tk.Button(button_frame, text="2", command=lambda: update("2"), padx=10)
button3 = tk.Button(button_frame, text="3", command=lambda: update("3"), padx=10)
button4 = tk.Button(button_frame, text="4", command=lambda: update("4"), padx=10)
button5 = tk.Button(button_frame, text="5", command=lambda: update("5"), padx=10)
button6 = tk.Button(button_frame, text="6", command=lambda: update("6"), padx=10)
button7 = tk.Button(button_frame, text="7", command=lambda: update("7"), padx=10)
button8 = tk.Button(button_frame, text="8", command=lambda: update("8"), padx=10)
button9 = tk.Button(button_frame, text="9", command=lambda: update("9"), padx=10)
button0 = tk.Button(button_frame, text="0", command=lambda: update("0"), padx=25)
button_alc = tk.Button(button_frame, text="AC", command=lambda: text.set(""), padx=5)
button_del = tk.Button(
    button_frame,
    text="Del",
    command=lambda: text.set(text.get()[:-1]),
    padx=3,
)
button_mod = tk.Button(button_frame, text="%", command=lambda: update("%"), padx=10)
button_add = tk.Button(button_frame, text="+", command=lambda: update("+"), padx=10)
button_sub = tk.Button(button_frame, text="-", command=lambda: update("-"), padx=10)
button_mul = tk.Button(button_frame, text="*", command=lambda: update("*"), padx=10)
button_div = tk.Button(button_frame, text="/", command=lambda: update("/"), padx=10)
button_dec = tk.Button(button_frame, text=".", command=lambda: update("."), padx=10)
button_res = tk.Button(button_frame, text="=", command=lambda: result(), padx=10)

# Displaying the buttons on the window using the grid geometry manager
button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=2, row=1)
button4.grid(column=0, row=2)
button5.grid(column=1, row=2)
button6.grid(column=2, row=2)
button7.grid(column=0, row=3)
button8.grid(column=1, row=3)
button9.grid(column=2, row=3)
button0.grid(column=0, row=4, columnspan=2)
button_alc.grid(column=0, row=0)
button_del.grid(column=1, row=0)
button_mod.grid(column=2, row=0)
button_add.grid(column=3, row=0)
button_sub.grid(column=3, row=1)
button_mul.grid(column=3, row=2)
button_div.grid(column=3, row=3)
button_dec.grid(column=2, row=4)
button_res.grid(column=3, row=4)

root.mainloop()
