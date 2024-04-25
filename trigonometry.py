from tkinter import ttk
import math

class Trigonometry:
    def __init__(self):
        self.trigonometry_combobox = ttk.Combobox(self.root, values=["sin", "cos", "tan"], font=("Menlo", 18),width=2, state="readonly")
        self.trigonometry_combobox.grid(row=3, columnspan=4, sticky="nesw")
        self.trigonometry_combobox.set("     Trigonometric Functions   ")
        self.trigonometry_combobox.bind("<<ComboboxSelected>>", self.apply_trigo)
        self.apply_trigo()
        
        
    def apply_trigo(self):
        selected_function = self.trigonometry_combobox.get()
        try:
            Radi = eval(f"math.radians({self.expression})")
            value = eval(f"math.{selected_function}({Radi})")
            result = float(value)
            result_var = str(result)
            self.previous_expression = f"{selected_function}({self.expression})"
            return str(result_var)
        except Exception as e:
            self.result_var = "Error"
            return result_var()

    def sin(self, value):
        try:
            tirgo = math.radians(float(value))
            result = math.sin(f'({float(tirgo)})')
            return str(result)
        except Exception as e:
            return "Error"

    def cos(self, value):
        try:
            tirgo = math.radians(float(value))
            result = math.cos(f'({float(tirgo)})')
            return str(result)
        except Exception as e:
            return "Error"

    def tan(self, value):
        try:
            tirgo = math.radians(float(value))
            result = math.tan(f'({float(tirgo)})')
            return str(result)
        except Exception as e:
            return "Error"

