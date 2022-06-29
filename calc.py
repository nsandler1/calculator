import tkinter
from tkinter import *
from tkinter import ttk

from enum import Enum, auto

DIM_FRAME = "450x450"
BUTTON_WIDTH = 2
BUTTON_FONT_SIZE = 32

class Calculator:
    class Operation(Enum):
        NUMBER = auto()
        ADD = "+"
        SUBTRACT = "-"
        DIVIDE = "/"
        MULTIPLY = "X"
        DECIMAL = "."
        EQUALS = "="
        CLEAR = "C"

        def __str__(self):
            return self.value

        @classmethod
        def _missing_(cls, _):
            return cls.NUMBER

    def __init__(self):
        self.queue = []
        self.label_text = None
        self.gui = self.init_gui()
        self.gui.mainloop()

    def init_gui(self):
        gui = Tk()
        gui.geometry(DIM_FRAME)
        display = ttk.Frame(gui, padding=10)
        btns = ttk.Frame(gui, padding=10)
        display.grid()
        btns.grid()

        self.label_text = StringVar(display, "test")
        ttk.Style().configure('TButton', font=('Helvetica', BUTTON_FONT_SIZE))
        ttk.Style().configure('TLabel', font=('Helvetica', BUTTON_FONT_SIZE))
        ttk.Label(display, relief="solid", textvariable=self.label_text).grid(column=0, row=0, columnspan=8, sticky=tkinter.W+tkinter.E)

        kwargs = {
            "width": BUTTON_WIDTH
        }

        def update_disp(val):
            operation = self.Operation(val)
            if operation is self.Operation.CLEAR:
                self.label_text = StringVar(display, "aa")
            else:
                self.label_text = StringVar(display, str(val))

        def clear():
            update_disp("C")

        def divide():
            update_disp("/")

        def mult():
            update_disp("X")

        def sub():
            update_disp("-")

        def add():
            update_disp("+")

        def decimal():
            update_disp(".")

        def one():
            update_disp("1")

        def two():
            update_disp("2")

        def three():
            update_disp("3")

        def four():
            update_disp("4")

        def five():
            update_disp("5")

        def six():
            update_disp("6")

        def seven():
            update_disp("7")

        def eight():
            update_disp("8")

        def nine():
            update_disp("9")

        def zero():
            update_disp("0")


        ttk.Button(btns, text="C", command=clear, **kwargs).grid(column=0, row=0)
        ttk.Button(btns, text="(", command=gui.destroy, **kwargs).grid(column=1, row=0)
        ttk.Button(btns, text=")", command=gui.destroy, **kwargs).grid(column=2, row=0)
        ttk.Button(btns, text="/", command=divide, **kwargs).grid(column=3, row=0)

        ttk.Button(btns, text="7", command=seven, **kwargs).grid(column=0, row=1)
        ttk.Button(btns, text="8", command=eight, **kwargs).grid(column=1, row=1)
        ttk.Button(btns, text="9", command=nine, **kwargs).grid(column=2, row=1)
        ttk.Button(btns, text="X", command=mult, **kwargs).grid(column=3, row=1)

        ttk.Button(btns, text="4", command=four, **kwargs).grid(column=0, row=2)
        ttk.Button(btns, text="5", command=five, **kwargs).grid(column=1, row=2)
        ttk.Button(btns, text="6", command=six, **kwargs).grid(column=2, row=2)
        ttk.Button(btns, text="-", command=sub, **kwargs).grid(column=3, row=2)

        ttk.Button(btns, text="1", command=one, **kwargs).grid(column=0, row=3)
        ttk.Button(btns, text="2", command=two, **kwargs).grid(column=1, row=3)
        ttk.Button(btns, text="3", command=three, **kwargs).grid(column=2, row=3)
        ttk.Button(btns, text="+", command=add, **kwargs).grid(column=3, row=3)

        ttk.Button(btns, text="0", command=zero, **kwargs).grid(
            column=0,
            row=4,
            columnspan=2,
            sticky=tkinter.W+tkinter.E
        )
        ttk.Button(btns, text=".", command=decimal, **kwargs).grid(column=2, row=4)
        ttk.Button(btns, text="=", command=self.calculate, **kwargs).grid(column=3, row=4)

        ttk.Button(btns, text="Quit", command=gui.destroy, **kwargs).grid(
            column=0,
            row=5,
            columnspan=4,
            sticky=tkinter.W+tkinter.E
        )

        gui.rowconfigure((0,1), weight=1)  # make buttons stretch when window is resized
        gui.columnconfigure((0,2), weight=1)

        return gui

    def calculate(self):
        pass


if __name__ == "__main__":
    calc = Calculator()
