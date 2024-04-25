import tkinter as tk
from tkinter import ttk
from date_button import date
#from chatgpt import ChatGPT
import math

class Calculator():
    def __init__(self, root, logic, date_button):
        self.root = root
        self.root.title("OLE - Calculator")
        self.root.geometry("375x667")
        self.root.iconphoto(False, tk.PhotoImage(file="OLElogo.png"))
        
        self.logic = logic
        #self.calculate_extreme_points()
        #self.chatgpt = chatgpt
        
        self.expression_var = tk.StringVar()
        self.expression_var.set("")
        
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        self.create_widgets()
        
        self.date_button = date_button
              
    def create_widgets(self):
        expression_label = tk.Label(self.root, textvariable=self.expression_var, font=("Menlo", 18, "bold"), anchor="nw", padx=10,bg=("#E8F1F0"), fg=("#00322C"))
        expression_label.grid(row=1 ,column=0, columnspan=5, sticky="nsew")
        
        
        result_label = tk.Label(self.root, textvariable=self.result_var, font=("Menlo", 42, "bold"), anchor="center", padx=10,bg=("#E8F1F0"), fg=("#00322C"))
        result_label.grid(row=2, column=0, columnspan=5, sticky="nsew")
        
       
        self.trigonometry_combobox = ttk.Combobox(self.root, values=["sin", "cos", "tan"], font=("Menlo", 18), width=10, state="readonly")
        self.trigonometry_combobox.grid(row=3, column=0, columnspan=4, sticky="nesw")
        self.trigonometry_combobox.set("Trigonometric Functions")
        self.trigonometry_combobox.bind("<<ComboboxSelected>>", self.apply_trigo)
        
        
        button_width = 2
        button_height = 1
        buttons = [ 
            ("√", 5, 0), ("^2", 5, 1), ("log", 5, 2), ("/", 5, 3),
            ("7", 6, 0), ("8", 6, 1), ("9", 6, 2), ("*", 6, 3),
            ("4", 7, 0), ("5", 7, 1), ("6", 7, 2), ("+", 7, 3),
            ("1", 8, 0), ("2", 8, 1), ("3", 8, 2), ("-", 8, 3),
            ("C", 9, 0), ("0", 9, 1), ("=", 9, 2),
            ("ChatGPT \n Finding Extreme Points", 10, 0)
            ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Menlo", 30, "bold"), width=button_width, height=button_height, 
                               padx=20, pady=20, command=lambda t=text: self.on_button_click(t), fg="#28403C")
            button.grid(row=row, column=col, sticky="nsew")
            
            if text == "+":
                button = tk.Button(self.root, text="+", font=("Menlo", 26, "bold"), width=button_width, height=button_height, 
                                   padx=20, pady=20, command=lambda t=text: self.on_button_click(t), fg="#456D67")
                button.grid(row=row, column=col, columnspan=2, sticky="nsew")
                
            if text == "-":
                button = tk.Button(self.root, text="-", font=("Menlo", 26, "bold"), width=button_width, height=button_height, 
                                   padx=20, pady=20, command=lambda t=text: self.on_button_click(t), fg="#456D67")
                button.grid(row=row, column=col, columnspan=2, sticky="nsew")
                
            if text == "*":
                button = tk.Button(self.root, text="x", font=("Menlo", 26, "bold"), width=button_width, height=button_height, 
                                   padx=20, pady=20, command=lambda t=text: self.on_button_click(t), fg="#456D67")
                button.grid(row=row, column=col, columnspan=2, sticky="nsew")
            
            if text == "/":
                button = tk.Button(self.root, text="÷", font=("Menlo", 26, "bold"), width=button_width, height=button_height, 
                                   padx=20, pady=20, command=lambda t=text: self.on_button_click(t), fg="#456D67")
                button.grid(row=row, column=col, columnspan=2, sticky="nsew")
            
            if text == "=":
                button = tk.Button(self.root, text=text, font=("Menlo", 40, "bold"), width=button_width, height=button_height, 
                                   padx=20, pady=20, command=lambda t=text: self.on_button_click(t), fg="#456D67")
                button.grid(row=row, column=col, columnspan=2, sticky="nsew")
            
            if text == "^2":
                button = tk.Button(self.root, text="x\u00b2", font=("Menlo", 26, "bold"), width=button_width, height=button_height, 
                                   padx=20, pady=20, command=lambda t=text: self.on_button_click(t), fg="#456D67")
                button.grid(row=row, column=col, sticky="nsew")
                
            if text == "√":
                button = tk.Button(self.root, text="\u221ax", font=("Menlo", 26, "bold"), width=button_width, height=button_height, 
                                   padx=20, pady=20, command=lambda t=text: self.on_button_click(t), fg="#456D67")
                button.grid(row=row, column=col, sticky="nsew")
            
            if text == "log":
                button = tk.Button(self.root, text="log", font=("Menlo", 26, "bold"), width=button_width, height=button_height, 
                                   padx=20, pady=20, command=lambda t=text: self.on_button_click(t), fg="#456D67")
                button.grid(row=row, column=col, sticky="nsew")
                
            if text == "ChatGPT \n Finding Extreme Points":
                button = tk.Button(self.root, text=text, font=("Menlo", 20, "bold"), width=button_width, height=button_height, 
                                   padx=20, pady=20, command=lambda t=text: self.on_button_click(t), fg="#456D67")
                button.grid(row=row, column=col, columnspan=4, sticky="nsew")
              
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)

    def display_date(self):
        today = date.today

    '''
    def calculate_extreme_points(self):
        
        a = float(self.entry_a.get())
        b = float(self.entry_b.get())
        c = float(self.entry_c.get())

        result = chatbot.find_extreme_points(a, b, c)
        result_label.config(text=result)
    '''   

    def on_button_click(self, text):

        if text == "=":
            result = self.logic.evaluate()
            self.result_var.set(result)
            self.logic.expression = result 
            self.expression_var.set("")
        
        elif text == "C":
            self.result_var.set("0")
            self.expression = ""
            self.expression_var.set("")
            
        elif text == "√":
            self.expression_var.set(f"√({self.logic.expression})")
            result = self.logic.sqrt_root()
            self.result_var.set(result)
            self.logic.expression = result
            
        elif text == "^2":
            self.expression_var.set(f"({self.logic.expression})\u00b2")
            result = self.logic.power(2)
            self.result_var.set(result)
            self.logic.expression = result
                 
        elif text == "log":
            self.expression_var.set(f"log({self.logic.expression})")
            result = self.logic.logarithm()
            self.result_var.set(result)
            self.logic.expression = result
              
        elif text == "ChatGPT \n Finding Extreme Points":
            self.chatgpt.calculate_extreme_points()
        
        else:
            if self.result_var.get() == "0" or self.logic.evaluate() == "Error":
                self.result_var.set(text)
            else:
                current_text = self.result_var.get()
                self.result_var.set(current_text + text)
            self.logic.expression += text
            self.expression_var.set(self.logic.expression)
    
    def apply_trigo(self, event):
        selected_function = self.trigonometry_combobox.get()
        if self.logic.expression:
            try:
                value = float(eval(self.logic.expression))
                radians = math.radians(value)
                if selected_function == "sin":
                    result = math.sin(radians)
                elif selected_function == "cos":
                    result = math.cos(radians)
                elif selected_function == "tan":
                    result = math.tan(radians)
                self.result_var.set(result)
                self.expression_var.set(f"{selected_function}({self.logic.expression})")
                self.logic.expression = str(result)
            except Exception as e:
                self.result_var.set("Error")