import tkinter as tk

import platform
from enum import Enum, auto
from functools import partial


GUI_DIM = "264x450"
BUTTON_WIDTH = 2
BUTTON_FONT_SIZE = 32
DISP_WIDTH = 10 # in character widths

class OS(Enum):
    WINDOWS = "Windows"
    MAC = "Darwin"
    LINUX = "Linux"

class Number():
    def __init__(self, arg1, arg2=None):
        self.arg1 = arg1
        self.arg2 = arg2

    @property
    def value(self):
        return int(self.arg1) if self.arg2 is None else float(f"{self.arg1}.{self.arg2}")

class Calculator():
    class Operation(Enum):
        NUMBER = auto()
        ADD = "+"
        SUBTRACT = "-"
        DIVIDE = "/"
        MULTIPLY = "*"
        L_PAREN = "("
        R_PAREN = ")"
        DECIMAL = "."
        EQUALS = "="
        BACKSPACE = "del"

        def __str__(self):
            return self.value

        def eval(self, arg1, arg2):
            if self is self.MULTIPLY:
                return arg1 * arg2
            elif self is self.DIVIDE:
                return arg1 / arg2
            elif self is self.ADD:
                return arg1 + arg2
            elif self is self.SUBTRACT:
                return arg1 - arg2

        @classmethod
        def pemdas(cls):
            return (cls.L_PAREN, cls.R_PAREN, cls.MULTIPLY, cls.DIVIDE, cls.ADD, cls.SUBTRACT)

        @classmethod
        def _missing_(cls, val):
            return cls.NUMBER


    def __init__(self):
        os = OS(platform.system())
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
            "fg": "black" if os is not OS.WINDOWS else "#white",
            "bg": "#a6a6a6",
            **kwargs
        }

        kwargs_secondary = {
            "fg": "black" if os is not OS.WINDOWS else "#white",
            "bg": "#7a7a7a",
            **kwargs
        }

        kwargs_operations = {
            "fg": "black",
            "bg": "#fc9d53",
            **kwargs
        }

        kwargs_warning = {
            "fg": "black" if os is not OS.WINDOWS else "#white",
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
        tk.Button(self.gui, text="*", command=partial(self.update_disp, "*"), **kwargs_operations).grid(column=3, row=2)

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
        new_text = ''.join([item for item in self.memory[1 - DISP_WIDTH:]])

        operation = self.Operation(val)
        if operation is self.Operation.BACKSPACE:
            new_text = new_text[:-1]
            self.memory = self.memory[:-1]
        elif operation is self.Operation.DECIMAL and self.memory.count(operation.value) > 0:
            mem_cpy = self.memory.copy()
            mem_cpy.reverse()
            slice_idx = mem_cpy.index(operation.value)
            if any(self.Operation(op) in self.Operation.pemdas() for op in mem_cpy[:slice_idx]):
                new_text += val
                self.memory.append(val)
        else:
            new_text += val
            self.memory.append(val)


        self.display.configure(text=new_text)
        self.display.update()

    def clear(self):
        self.display.configure(text="0")
        self.memory.clear()
        self.display.update()

    def parse(self):
        # Parse integers

        def get_number(lst):
            str_ = ''.join(lst)
            if str_.count(self.Operation.DECIMAL.value) > 0:
                if len(lst) != 1:
                    return 0
                #point_idx = str_.index(self.Operation.DECIMAL.value)
                #num_digits = len(str_[point_idx + 1:])
                #ret = float(str_)
                #return round(ret, num_digits)
                return float(str_)

            return int(str_)

        parsed_mem = []
        while len(self.memory) > 0:
            idx = 0
            while idx < len(self.memory) and self.Operation(self.memory[idx]) is self.Operation.NUMBER:
                idx += 1

            if idx == 0:
                arg = get_number(self.memory)
            else:
                arg = get_number(self.memory[:idx])

            parsed_mem.append(arg)

            if idx < len(self.memory):
                op = self.Operation(self.memory[idx])
                parsed_mem.append(op)

            self.memory = self.memory[idx + 1:]
        print(parsed_mem)
        # Parse decimals
        while parsed_mem.count(self.Operation.DECIMAL) > 0:
            idx = parsed_mem.index(self.Operation.DECIMAL)
            arg1 = 0 if self.Operation(parsed_mem[idx - 1]) is not self.Operation.NUMBER else parsed_mem[idx - 1]
            new_val = float(f"{arg1}.{parsed_mem[idx + 1]}")
            parsed_mem[idx + 1] = new_val

            # left-shift parsed_mem by 2
            for i in range(idx + 1, len(parsed_mem)):
                parsed_mem[i - 2] = parsed_mem[i]

            parsed_mem = parsed_mem[:len(parsed_mem) - 2]

        print(parsed_mem)

        return parsed_mem

    def calculate(self):
        # TODO: Parse parenthesis

        parsed_mem = self.parse()
        for operation in self.Operation.pemdas()[2:]:
            while parsed_mem.count(operation) > 0:
                idx = parsed_mem.index(operation)
                res = operation.eval(parsed_mem[idx - 1], parsed_mem[idx + 1])
                parsed_mem[idx + 1] = res

                # left-shift parsed_mem by 2
                for i in range(idx + 1, len(parsed_mem)):
                    parsed_mem[i - 2] = parsed_mem[i]

                parsed_mem = parsed_mem[:len(parsed_mem) - 2]

        self.display.configure(text=str(parsed_mem[0]))
        self.display.update()
        self.memory.clear()
        self.memory.append(str(parsed_mem[0]))


if __name__ == "__main__":
    calc = Calculator()
