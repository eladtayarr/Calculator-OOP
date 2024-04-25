import tkinter as tk

from date_button import DateButton
from calculator_logic import CalculatorLogic
from calculator import Calculator
from chatgpt import ChatGPT

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.date_button = DateButton(self.root)
        #self.chatgpt = ChatGPT()
        self.logic = CalculatorLogic()
        self.calculator = Calculator(self.root, self.logic, self.date_button)
        self.root.mainloop()


if __name__ == "__main__":
    app = MainApp()
