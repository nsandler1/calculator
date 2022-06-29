import tkinter
from tkinter import *
from tkinter import ttk

from enum import Enum, auto

DIM_FRAME = "450x450"
BUTTON_WIDTH = 2
BUTTON_FONT_SIZE = 32

class Calculator:
    class Operation(Enum):
        ADD = auto()
        SUBTRACT = auto()
        DIVIDE = auto()
        MULTIPLY = auto()
        DECIMAL = auto()
        EQUALS = auto()
        CLEAR = auto()

    def __init__(self):
        self.queue = []
        self.gui = self.init_gui()
        self.gui.mainloop()

    def init_gui(self):
        gui = Tk()
        gui.geometry(DIM_FRAME)
        display = ttk.Frame(gui, padding=10, border=20)
        btns = ttk.Frame(gui, padding=10)
        display.grid()
        btns.grid()

        ttk.Style().configure('TButton', font=('Helvetica', BUTTON_FONT_SIZE))
        ttk.Style().configure('TLabel', font=('Helvetica', BUTTON_FONT_SIZE))
        ttk.Label(display, text="Hello World!").grid(column=0, row=0, columnspan=4)

        kwargs = {
            "width": BUTTON_WIDTH
        }


        ttk.Button(btns, text="Clear", command=gui.destroy, **kwargs).grid(
            column=0,
            row=0,
            columnspan=3,
            sticky=tkinter.W+tkinter.E
        )
        ttk.Button(btns, text="/", command=gui.destroy, **kwargs).grid(column=3, row=0)

        ttk.Button(btns, text="7", command=gui.destroy, **kwargs).grid(column=0, row=1)
        ttk.Button(btns, text="8", command=gui.destroy, **kwargs).grid(column=1, row=1)
        ttk.Button(btns, text="9", command=gui.destroy, **kwargs).grid(column=2, row=1)
        ttk.Button(btns, text="X", command=gui.destroy, **kwargs).grid(column=3, row=1)

        ttk.Button(btns, text="4", command=gui.destroy, **kwargs).grid(column=0, row=2)
        ttk.Button(btns, text="5", command=gui.destroy, **kwargs).grid(column=1, row=2)
        ttk.Button(btns, text="6", command=gui.destroy, **kwargs).grid(column=2, row=2)
        ttk.Button(btns, text="-", command=gui.destroy, **kwargs).grid(column=3, row=2)

        ttk.Button(btns, text="1", command=gui.destroy, **kwargs).grid(column=0, row=3)
        ttk.Button(btns, text="2", command=gui.destroy, **kwargs).grid(column=1, row=3)
        ttk.Button(btns, text="3", command=gui.destroy, **kwargs).grid(column=2, row=3)
        ttk.Button(btns, text="+", command=gui.destroy, **kwargs).grid(column=3, row=3)

        ttk.Button(btns, text="0", command=gui.destroy, **kwargs).grid(
            column=0,
            row=4,
            columnspan=2,
            sticky=tkinter.W+tkinter.E
        )
        ttk.Button(btns, text=".", command=gui.destroy, **kwargs).grid(column=2, row=4)
        ttk.Button(btns, text="=", command=gui.destroy, **kwargs).grid(column=3, row=4)

        #gui.rowconfigure((0,1), weight=1)  # make buttons stretch when window is resized
        #gui.columnconfigure((0,2), weight=1)
        return gui


calc = Calculator()
