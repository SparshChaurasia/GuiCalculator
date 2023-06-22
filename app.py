import tkinter as tk
from math import sqrt
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
        self.last_operation = tk.StringVar()

        self.geometry("225x273")
        self.title("Calculator")

        self.top = tk.Frame(self)
        self.top.grid(row=3, column=0, sticky="E")

        self.textarea1 = tk.Label(
            self, textvariable=self.last_operation, justify=tk.RIGHT
        )
        self.textarea1.grid(row=0, columnspan=2, sticky="EW")
        # Main textarea to display all the text on the screen
        self.textarea = tk.Label(
            self, textvariable=self.text, bg="white", justify=tk.RIGHT
        )
        self.textarea.grid(row=1, columnspan=2, sticky="EW")

        # GUI component that contains all menu buttons
        self.menu = tk.Frame(self)
        self.menu.grid(row=2, columnspan=2)

        # GUI element to hold all the calculator buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=3, column=1)

        # Creating buttons on the menu component
        self.memory_add = tk.Button(
            self.top, text="M+", height=2, width=5, command=self.add_memory
        )
        self.memory_subtract = tk.Button(
            self.top, text="M-", height=2, width=5, command=self.clear_memory
        )
        self.memory_recall = tk.Button(
            self.top, text="MR", height=2, width=5, command=self.clear_memory
        )
        self.memory_recall_clear = tk.Button(
            self.top, text="MRC", height=2, width=5, command=self.recall_memory
        )
        self.button_ce = tk.Button(
            self.top,
            text="CE",
            command=lambda: self.text.set(""),
            height=2,
            width=5,
        )
        self.history = tk.Button(
            self.menu,
            text="History",
            height=1,
            width=5,
            command=Calculator.show_history,
        )
        self.button_alc = tk.Button(
            self.menu,
            text="AC",
            command=lambda: self.text.set(""),
            height=1,
            width=5,
        )
        self.button_del = tk.Button(
            self.menu,
            text="Del",
            command=lambda: self.text.set(self.text.get()[:-1]),
            height=1,
            width=5,
        )
        self.button_pow = tk.Button(
            self.menu,
            text="pow",
            command=lambda: self.update("**"),
            height=1,
            width=5,
        )
        self.button_sqrt = tk.Button(
            self.menu,
            text="√",
            command=lambda: self.update("sqrt("),
            height=1,
            width=5,
        )
        # Displaying the buttons on the window using the grid geometry manager
        self.memory_recall.grid(column=0, row=0)
        self.memory_recall_clear.grid(column=0, row=1)
        self.memory_subtract.grid(column=0, row=2)
        self.memory_add.grid(column=0, row=3)
        self.button_ce.grid(column=0, row=4)

        self.history.grid(column=0, row=0)
        self.button_pow.grid(column=1, row=0)
        self.button_sqrt.grid(column=2, row=0)
        self.button_alc.grid(column=3, row=0)
        self.button_del.grid(column=4, row=0)

        # Creating all the buttons for numbers and utility
        self.button1 = tk.Button(
            self.button_frame,
            text="1",
            command=lambda: self.update("1"),
            height=2,
            width=5,
        )
        self.button2 = tk.Button(
            self.button_frame,
            text="2",
            command=lambda: self.update("2"),
            height=2,
            width=5,
        )
        self.button3 = tk.Button(
            self.button_frame,
            text="3",
            command=lambda: self.update("3"),
            height=2,
            width=5,
        )
        self.button4 = tk.Button(
            self.button_frame,
            text="4",
            command=lambda: self.update("4"),
            height=2,
            width=5,
        )
        self.button5 = tk.Button(
            self.button_frame,
            text="5",
            command=lambda: self.update("5"),
            height=2,
            width=5,
        )
        self.button6 = tk.Button(
            self.button_frame,
            text="6",
            command=lambda: self.update("6"),
            height=2,
            width=5,
        )
        self.button7 = tk.Button(
            self.button_frame,
            text="7",
            command=lambda: self.update("7"),
            height=2,
            width=5,
        )
        self.button8 = tk.Button(
            self.button_frame,
            text="8",
            command=lambda: self.update("8"),
            height=2,
            width=5,
        )
        self.button9 = tk.Button(
            self.button_frame,
            text="9",
            command=lambda: self.update("9"),
            height=2,
            width=5,
        )
        self.button0 = tk.Button(
            self.button_frame,
            text="0",
            command=lambda: self.update("0"),
            height=2,
            width=5,
        )
        self.button00 = tk.Button(
            self.button_frame,
            text="00",
            command=lambda: self.update("00"),
            height=2,
            width=5,
        )
        self.bracket_open = tk.Button(
            self.button_frame,
            text="(",
            command=lambda: self.update("("),
            height=2,
            width=5,
        )
        self.bracket_close = tk.Button(
            self.button_frame,
            text=")",
            command=lambda: self.update(")"),
            height=2,
            width=5,
        )
        self.button_mod = tk.Button(
            self.button_frame,
            text="%",
            command=lambda: self.update("%"),
            height=2,
            width=5,
        )
        self.button_add = tk.Button(
            self.button_frame,
            text="+",
            command=lambda: self.update("+"),
            height=2,
            width=5,
        )
        self.button_sub = tk.Button(
            self.button_frame,
            text="-",
            command=lambda: self.update("-"),
            height=2,
            width=5,
        )
        self.button_mul = tk.Button(
            self.button_frame,
            text="*",
            command=lambda: self.update("*"),
            height=2,
            width=5,
        )
        self.button_div = tk.Button(
            self.button_frame,
            text="/",
            command=lambda: self.update("/"),
            height=2,
            width=5,
        )
        self.button_dec = tk.Button(
            self.button_frame,
            text=".",
            command=lambda: self.update("."),
            height=2,
            width=5,
        )
        self.button_res = tk.Button(
            self.button_frame,
            text="=",
            command=lambda: self.result(),
            height=2,
            width=5,
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
        self.button0.grid(column=0, row=4)
        self.button00.grid(column=1, row=4)
        self.bracket_open.grid(column=0, row=0)
        self.bracket_close.grid(column=1, row=0)
        self.button_mod.grid(column=2, row=0)
        self.button_add.grid(column=3, row=0)
        self.button_sub.grid(column=3, row=1)
        self.button_mul.grid(column=3, row=2)
        self.button_div.grid(column=3, row=3)
        self.button_dec.grid(column=2, row=4)
        self.button_res.grid(column=3, row=4)

    # Function to update the textbox on button press
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
            self.last_operation.set(_text + "=")
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
