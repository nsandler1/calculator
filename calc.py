from tkinter import *
from tkinter import ttk

from enum import Enum, auto
import tkinter

DIM_FRAME = "450x450"
BUTTON_WIDTH = 4
BUTTON_FONT_SIZE = 32

class Operation(Enum):
    ADD = auto()
    SUBTRACT = auto()
    DIVIDE = auto()
    MULTIPLY = auto()
    DECIMAL = auto()
    EQUALS = auto()
    CLEAR = auto()


root = Tk()
root.geometry(DIM_FRAME)
display = ttk.Frame(root, padding=10, border=20)
btns = ttk.Frame(root, padding=10)
display.grid()
btns.grid()

ttk.Style().configure('TButton', font=('Helvetica', BUTTON_FONT_SIZE))
ttk.Style().configure('TLabel', font=('Helvetica', BUTTON_FONT_SIZE))
ttk.Label(display, text="Hello World!").grid(column=0, row=0, columnspan=4)

kwargs = {
    "width": BUTTON_WIDTH
}


ttk.Button(btns, text="Quit", command=root.destroy, **kwargs).grid(column=0, row=0)
ttk.Button(btns, text="Clr", command=root.destroy, **kwargs).grid(column=1, row=0)
ttk.Button(btns, text="?", command=root.destroy, **kwargs).grid(column=2, row=0)
ttk.Button(btns, text="/", command=root.destroy, **kwargs).grid(column=3, row=0)

ttk.Button(btns, text="7", command=root.destroy, **kwargs).grid(column=0, row=1)
ttk.Button(btns, text="8", command=root.destroy, **kwargs).grid(column=1, row=1)
ttk.Button(btns, text="9", command=root.destroy, **kwargs).grid(column=2, row=1)
ttk.Button(btns, text="X", command=root.destroy, **kwargs).grid(column=3, row=1)

ttk.Button(btns, text="4", command=root.destroy, **kwargs).grid(column=0, row=2)
ttk.Button(btns, text="5", command=root.destroy, **kwargs).grid(column=1, row=2)
ttk.Button(btns, text="6", command=root.destroy, **kwargs).grid(column=2, row=2)
ttk.Button(btns, text="-", command=root.destroy, **kwargs).grid(column=3, row=2)

ttk.Button(btns, text="1", command=root.destroy, **kwargs).grid(column=0, row=3)
ttk.Button(btns, text="2", command=root.destroy, **kwargs).grid(column=1, row=3)
ttk.Button(btns, text="3", command=root.destroy, **kwargs).grid(column=2, row=3)
ttk.Button(btns, text="+", command=root.destroy, **kwargs).grid(column=3, row=3)

ttk.Button(btns, text="0", command=root.destroy, **kwargs).grid(column=0, row=4, columnspan=2, sticky=tkinter.W+tkinter.E)
ttk.Button(btns, text=".", command=root.destroy, **kwargs).grid(column=2, row=4)
ttk.Button(btns, text="=", command=root.destroy, **kwargs).grid(column=3, row=4)

#root.rowconfigure((0,1), weight=1)  # make buttons stretch when window is resized
#root.columnconfigure((0,2), weight=1)

root.mainloop()
