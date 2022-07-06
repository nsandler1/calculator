import tkinter as tk

from enum import Enum, auto
from functools import partial

GUI_DIM = "264x450"
BUTTON_WIDTH = 2
BUTTON_FONT_SIZE = 32
DISP_WIDTH = 10 # in character widths

class Calculator():
    class Operation(Enum):
        NUMBER = auto()
        ADD = "+"
        SUBTRACT = "-"
        DIVIDE = "/"
        MULTIPLY = "x"
        DECIMAL = "."
        EQUALS = "="
        BACKSPACE = "del"

        def __str__(self):
            return self.value

        @classmethod
        def _missing_(cls, _):
            return cls.NUMBER

    def __init__(self):
        self.memory = []
        self.gui = tk.Tk()
        self.gui.geometry(GUI_DIM)

        self.display = tk.Label(self.gui, relief="solid", width=DISP_WIDTH, font=f"Helvetica {BUTTON_FONT_SIZE}", text="0")
        self.display.grid(column=0, row=0, columnspan=4, sticky=tk.W+tk.E)

        kwargs = {
            "image": tk.PhotoImage(width=1, height=1),
            "font": f"Helvetica {BUTTON_FONT_SIZE}",
            "width": 50,
            "height": 50,
            "compound": "c",
            "padx": 5,
            "pady": 5
        }

        kwargs_primary = {
            "fg": "white",
            "bg": "#a6a6a6",
            **kwargs
        }

        kwargs_secondary = {
            "fg": "white",
            "bg": "#7a7a7a",
            **kwargs
        }

        kwargs_operations = {
            "fg": "black",
            "bg": "#fc9d53",
            **kwargs
        }

        kwargs_warning = {
            "fg": "white",
            "bg": "#ff6363",
            **kwargs
        }
        tk.Button(self.gui, text="C", command=self.clear, **kwargs_secondary).grid(column=0, row=1)
        tk.Button(self.gui, text="(", command=partial(self.update_disp, "("), **kwargs_operations).grid(column=1, row=1)
        tk.Button(self.gui, text=")", command=partial(self.update_disp, ")"), **kwargs_operations).grid(column=2, row=1)
        tk.Button(self.gui, text="/", command=partial(self.update_disp, "/"), **kwargs_operations).grid(column=3, row=1)

        tk.Button(self.gui, text="7", command=partial(self.update_disp, "7"), **kwargs_primary).grid(column=0, row=2)
        tk.Button(self.gui, text="8", command=partial(self.update_disp, "8"), **kwargs_primary).grid(column=1, row=2)
        tk.Button(self.gui, text="9", command=partial(self.update_disp, "9"), **kwargs_primary).grid(column=2, row=2)
        tk.Button(self.gui, text="X", command=partial(self.update_disp, "x"), **kwargs_operations).grid(column=3, row=2)

        tk.Button(self.gui, text="4", command=partial(self.update_disp, "4"), **kwargs_primary).grid(column=0, row=3)
        tk.Button(self.gui, text="5", command=partial(self.update_disp, "5"), **kwargs_primary).grid(column=1, row=3)
        tk.Button(self.gui, text="6", command=partial(self.update_disp, "6"), **kwargs_primary).grid(column=2, row=3)
        tk.Button(self.gui, text="-", command=partial(self.update_disp, "-"), **kwargs_operations).grid(column=3, row=3)

        tk.Button(self.gui, text="1", command=partial(self.update_disp, "1"), **kwargs_primary).grid(column=0, row=4)
        tk.Button(self.gui, text="2", command=partial(self.update_disp, "2"), **kwargs_primary).grid(column=1, row=4)
        tk.Button(self.gui, text="3", command=partial(self.update_disp, "3"), **kwargs_primary).grid(column=2, row=4)
        tk.Button(self.gui, text="+", command=partial(self.update_disp, "+"), **kwargs_operations).grid(column=3, row=4)

        tk.Button(self.gui, text="0", command=partial(self.update_disp, "0"), **kwargs_primary).grid(
            column=0,
            row=5,
            columnspan=2,
            sticky=tk.W+tk.E
        )
        tk.Button(self.gui, text=".", command=partial(self.update_disp, "."), **kwargs_primary).grid(column=2, row=5)
        tk.Button(self.gui, text="=", command=self.calculate, **kwargs_operations).grid(column=3, row=5)

        tk.Button(self.gui, text="Quit", command=self.gui.destroy, **kwargs_warning).grid(
            column=0,
            row=6,
            columnspan=2,
            sticky=tk.W+tk.E
        )

        tk.Button(self.gui, text="del", command=partial(self.update_disp, "del"), **kwargs_secondary).grid(
            column=2,
            row=6,
            columnspan=2,
            sticky=tk.W+tk.E
        )

        self.gui.mainloop()

    def update_disp(self, val):
        # TODO: prevent decimals from being placed multiple times in one number
        # EX: 32.533.4
        new_text = ''.join([item for item in self.memory[1 - DISP_WIDTH:]])

        op = self.Operation(val)
        if op is self.Operation.BACKSPACE:
            new_text = new_text[:-1]
            self.memory = self.memory[:-1]
        else:
            new_text += val
            self.memory.append(val)


        self.display.configure(text=new_text)
        self.display.update()

    def clear(self):
        self.display.configure(text="")
        self.memory.clear()
        self.display.update()

    def calculate(self):
        # Parse integers
        parsed_mem = []
        print(self.memory)
        while len(self.memory) > 0:
            idx = 0
            while idx < len(self.memory) and self.Operation(self.memory[idx]) is self.Operation.NUMBER:
                idx += 1

            try:
                arg = int(''.join(self.memory[:idx]))
            except ValueError:
                arg = 0

            parsed_mem.append(arg)

            if idx < len(self.memory):
                op = self.Operation(self.memory[idx])
                parsed_mem.append(op)

            self.memory = self.memory[idx + 1:]

        print(parsed_mem)

        # Parse decimals
        # Validation:
        #   - prohibit multiple decimals in a single number

        while parsed_mem.count(self.Operation.DECIMAL) > 0:
            idx = parsed_mem.index(self.Operation.DECIMAL)
            new_val = float(f"{parsed_mem[idx - 1]}.{parsed_mem[idx + 1]}")
            parsed_mem.insert(idx + 2, new_val)

            # left-shift parsed_mem by 2
            for i in range(idx + 2, len(parsed_mem)):
                parsed_mem[i - 3] = parsed_mem[i]

            parsed_mem = parsed_mem[:len(parsed_mem) - 3]

        print(parsed_mem)

        # TODO: Parse parenthesis

        # TODO: Execute calculation


if __name__ == "__main__":
    calc = Calculator()
