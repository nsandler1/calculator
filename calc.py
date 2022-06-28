from tkinter import *
from tkinter import ttk

from enum import Enum, auto

class Action(Enum):
    ADD = auto()
    SUBTRACT = auto()
    DIVIDE = auto()
    MULTIPLY = auto()


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
