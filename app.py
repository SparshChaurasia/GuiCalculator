import tkinter as tk
from tkinter import messagebox


class Calculator(tk.Tk):
    """
    Class to group the functionality of a calculator
    """

    def __init__(self):
        # Creates an instance of a new GUI window
        super().__init__()

        self.memory: str
        self.text = tk.StringVar()  # Varible to hold the text on the screen

        self.geometry("200x175")
        self.title("Calculator")

        # GUI component that contains all buttons on the left
        self.menu = tk.Frame(self)
        self.menu.pack(side=tk.LEFT)

        # Creating buttons on the menu component
        self.btn1 = tk.Button(
            self.menu,
            text="History",
            height=2,
            width=5,
            command=Calculator.show_history,
        )
        self.btn2 = tk.Button(
            self.menu, text="M+", height=2, width=5, command=self.add_memory
        )
        self.btn3 = tk.Button(
            self.menu, text="M-", height=2, width=5, command=self.clear_memory
        )
        self.btn4 = tk.Button(
            self.menu, text="MRC", height=2, width=5, command=self.recall_memory
        )

        # Displaying the buttons on the window using the grid geometry manager
        self.btn1.grid(row=0)
        self.btn2.grid(row=1)
        self.btn3.grid(row=2)
        self.btn4.grid(row=3)

        # Main textarea to display all the text on the screen
        self.textarea = tk.Label(self, textvariable=self.text, bg="white")
        self.textarea.pack(fill="both", expand=True)

        # GUI element to hold all the calculator buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.pack()

        # Creating all the buttons for numbers and utility
        self.button1 = tk.Button(
            self.button_frame, text="1", command=lambda: self.update("1"), padx=10
        )
        self.button2 = tk.Button(
            self.button_frame, text="2", command=lambda: self.update("2"), padx=10
        )
        self.button3 = tk.Button(
            self.button_frame, text="3", command=lambda: self.update("3"), padx=10
        )
        self.button4 = tk.Button(
            self.button_frame, text="4", command=lambda: self.update("4"), padx=10
        )
        self.button5 = tk.Button(
            self.button_frame, text="5", command=lambda: self.update("5"), padx=10
        )
        self.button6 = tk.Button(
            self.button_frame, text="6", command=lambda: self.update("6"), padx=10
        )
        self.button7 = tk.Button(
            self.button_frame, text="7", command=lambda: self.update("7"), padx=10
        )
        self.button8 = tk.Button(
            self.button_frame, text="8", command=lambda: self.update("8"), padx=10
        )
        self.button9 = tk.Button(
            self.button_frame, text="9", command=lambda: self.update("9"), padx=10
        )
        self.button0 = tk.Button(
            self.button_frame, text="0", command=lambda: self.update("0"), padx=25
        )
        self.button_alc = tk.Button(
            self.button_frame, text="AC", command=lambda: self.text.set(""), padx=5
        )
        self.button_del = tk.Button(
            self.button_frame,
            text="Del",
            command=lambda: self.text.set(self.text.get()[:-1]),
            padx=3,
        )
        self.button_mod = tk.Button(
            self.button_frame, text="%", command=lambda: self.update("%"), padx=10
        )
        self.button_add = tk.Button(
            self.button_frame, text="+", command=lambda: self.update("+"), padx=10
        )
        self.button_sub = tk.Button(
            self.button_frame, text="-", command=lambda: self.update("-"), padx=10
        )
        self.button_mul = tk.Button(
            self.button_frame, text="*", command=lambda: self.update("*"), padx=10
        )
        self.button_div = tk.Button(
            self.button_frame, text="/", command=lambda: self.update("/"), padx=10
        )
        self.button_dec = tk.Button(
            self.button_frame, text=".", command=lambda: self.update("."), padx=10
        )
        self.button_res = tk.Button(
            self.button_frame, text="=", command=lambda: self.result(), padx=10
        )

        # Displaying the buttons on the window using the grid geometry manager
        self.button1.grid(column=0, row=1)
        self.button2.grid(column=1, row=1)
        self.button3.grid(column=2, row=1)
        self.button4.grid(column=0, row=2)
        self.button5.grid(column=1, row=2)
        self.button6.grid(column=2, row=2)
        self.button7.grid(column=0, row=3)
        self.button8.grid(column=1, row=3)
        self.button9.grid(column=2, row=3)
        self.button0.grid(column=0, row=4, columnspan=2)
        self.button_alc.grid(column=0, row=0)
        self.button_del.grid(column=1, row=0)
        self.button_mod.grid(column=2, row=0)
        self.button_add.grid(column=3, row=0)
        self.button_sub.grid(column=3, row=1)
        self.button_mul.grid(column=3, row=2)
        self.button_div.grid(column=3, row=3)
        self.button_dec.grid(column=2, row=4)
        self.button_res.grid(column=3, row=4)

    def update(self, string):
        _text = self.text.get() + string
        self.text.set(_text)

    # Functions to use the memory
    def add_memory(self):
        """
        Add to the memory
        :return: None
        """

        self.memory = self.text.get()

    def clear_memory(self):
        """Clears the memory"""

        self.memory = None

    def recall_memory(self):
        """Insert the memory value in the textbox"""

        _memory = self.memory if self.memory else ""
        self.update(_memory)

    @staticmethod
    def show_history():
        """Create a toplevel window and show the text in the data text file"""
        win = tk.Toplevel()
        win.geometry("100x100")
        with open("./data.txt", "r") as file:
            file_text = "".join(file.readlines())

        label = tk.Label(win, text=file_text)
        label.pack()
        win.mainloop()

    @staticmethod
    def add_to_history(operation, result):
        """Add an entry of a opertion in the data text file"""
        with open("./data.txt", "r+") as file:
            line = len(file.readlines())
            file.write(f"{line+1}) {operation} = {result}\n")

    def result(self):
        """Evaulate the expression and show a message if there are any errors"""

        _text = self.text.get()
        try:
            output = eval(_text)
            self.text.set(output)
            Calculator.add_to_history(_text, output)
        except NameError:
            messagebox.showwarning("Error", "Invalid syntax")
        except ZeroDivisionError:
            messagebox.showwarning("Error", "Could not divide by zero")
        except SyntaxError as e:
            messagebox.showwarning("Error", "Invalid syntax")


if __name__ == "__main__":
    c = Calculator()
    c.mainloop()
