from copy import deepcopy
import tkinter
from tkinter import *
from tkinter import ttk

from enum import Enum, auto
from functools import partial

GUI_DIM = "450x450"
BUTTON_WIDTH = 2
BUTTON_FONT_SIZE = 32
DISP_WIDTH = 10 # in character widths

class Calculator:
    class Operation(Enum):
        NUMBER = auto()
        ADD = "+"
        SUBTRACT = "-"
        DIVIDE = "/"
        MULTIPLY = "x"
        DECIMAL = "."
        EQUALS = "="

        def __str__(self):
            return self.value

        @classmethod
        def _missing_(cls, _):
            return cls.NUMBER

    def __init__(self):
        self.memory = []
        self.label = None
        self.label_text = ""
        self.gui = self.init_gui()
        self.gui.mainloop()

    def init_gui(self):
        gui = Tk()
        gui.geometry(GUI_DIM)
        display = ttk.Frame(gui, padding=10)
        keypad = ttk.Frame(gui, padding=10)
        display.grid()
        keypad.grid()

        ttk.Style().configure('TButton', font=('Helvetica', BUTTON_FONT_SIZE))
        ttk.Style().configure('TLabel', font=('Helvetica', BUTTON_FONT_SIZE))
        label = ttk.Label(display, relief="solid", width=DISP_WIDTH, text="")
        label.grid(column=0, row=0)

        kwargs = {
            "width": BUTTON_WIDTH
        }

        ttk.Button(keypad, text="C", command=self.clear, **kwargs).grid(column=0, row=0)
        ttk.Button(keypad, text="(", command=partial(self.update_disp, "("), **kwargs).grid(column=1, row=0)
        ttk.Button(keypad, text=")", command=partial(self.update_disp, ")"), **kwargs).grid(column=2, row=0)
        ttk.Button(keypad, text="/", command=partial(self.update_disp, "/"), **kwargs).grid(column=3, row=0)

        ttk.Button(keypad, text="7", command=partial(self.update_disp, "7"), **kwargs).grid(column=0, row=1)
        ttk.Button(keypad, text="8", command=partial(self.update_disp, "8"), **kwargs).grid(column=1, row=1)
        ttk.Button(keypad, text="9", command=partial(self.update_disp, "9"), **kwargs).grid(column=2, row=1)
        ttk.Button(keypad, text="X", command=partial(self.update_disp, "x"), **kwargs).grid(column=3, row=1)

        ttk.Button(keypad, text="4", command=partial(self.update_disp, "4"), **kwargs).grid(column=0, row=2)
        ttk.Button(keypad, text="5", command=partial(self.update_disp, "5"), **kwargs).grid(column=1, row=2)
        ttk.Button(keypad, text="6", command=partial(self.update_disp, "6"), **kwargs).grid(column=2, row=2)
        ttk.Button(keypad, text="-", command=partial(self.update_disp, "-"), **kwargs).grid(column=3, row=2)

        ttk.Button(keypad, text="1", command=partial(self.update_disp, "1"), **kwargs).grid(column=0, row=3)
        ttk.Button(keypad, text="2", command=partial(self.update_disp, "2"), **kwargs).grid(column=1, row=3)
        ttk.Button(keypad, text="3", command=partial(self.update_disp, "3"), **kwargs).grid(column=2, row=3)
        ttk.Button(keypad, text="+", command=partial(self.update_disp, "+"), **kwargs).grid(column=3, row=3)

        ttk.Button(keypad, text="0", command=partial(self.update_disp, "0"), **kwargs).grid(
            column=0,
            row=4,
            columnspan=2,
            sticky=tkinter.W+tkinter.E
        )
        ttk.Button(keypad, text=".", command=partial(self.update_disp, "."), **kwargs).grid(column=2, row=4)
        ttk.Button(keypad, text="=", command=self.calculate, **kwargs).grid(column=3, row=4)

        ttk.Button(keypad, text="Quit", command=gui.destroy, **kwargs).grid(
            column=0,
            row=5,
            columnspan=4,
            sticky=tkinter.W+tkinter.E
        )

        gui.rowconfigure((0,1), weight=1)  # make buttons stretch when window is resized
        gui.columnconfigure((0,2), weight=1)

        self.label = label
        return gui

    def update_disp(self, val):
        # TODO: prevent decimals from being placed multiple times in one number
        # EX: 32.533.4
        new_text = ''.join([item for item in self.memory[1 - DISP_WIDTH:]]) + val
        self.label.configure(text=new_text)
        self.memory.append(val)
        self.label.update()

    def clear(self):
        self.label.configure(text="")
        self.memory.clear()
        self.label.update()

    def calculate(self):
        # Parse integers
        parsed_mem = []
        while len(self.memory) > 0:
            idx = 0
            while idx < len(self.memory) and self.Operation(self.memory[idx]) is self.Operation.NUMBER:
                idx += 1

            arg = int(''.join(self.memory[:idx]))
            parsed_mem.append(arg)

            if idx < len(self.memory):
                op = self.Operation(self.memory[idx])
                parsed_mem.append(op)

            self.memory = self.memory[idx + 1:]

        print(parsed_mem)

        # Parse decimals
        while parsed_mem.count(self.Operation.DECIMAL) > 0:
            idx = parsed_mem.index(self.Operation.DECIMAL)
            new_val = float(f"{parsed_mem[idx - 1]}.{parsed_mem[idx + 1]}")
            parsed_mem.insert(idx + 2, new_val)

            for i in range(idx + 2, len(parsed_mem)): # left shift parsed_mem by 2
                parsed_mem[i - 3] = parsed_mem[i]

            parsed_mem = parsed_mem[:len(parsed_mem) - 2]

        parsed_mem = parsed_mem[:len(parsed_mem) - 2]
        print(parsed_mem)

        # TODO: Parse parenthesis

        # TODO: Execute calculation



if __name__ == "__main__":
    calc = Calculator()
