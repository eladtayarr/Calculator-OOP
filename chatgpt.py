import tkinter as tk
from openai import OpenAI
from calculator import Calculator
#Client = OpenAI()

class ChatGPT(Calculator):
    def __init__(self):
        self.Client = Client(api_key='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')
        self.completion = self.Client.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a calculator."},
                {"role": "user", "content": "Calculate the extreme points of a quadratic function."},
            ]
        )
        
        
    def find_extreme_points(self, a, b, c):
        user_message = f"Calculate the extreme points of the quadratic function f(x) = {a}x^2 + {b}x + {c}."
        response = self.completion.create(
            messages=[{"role": "user", "content": user_message}],
            max_tokens=100,
        )
        return response['choices'][0]['message']['content']
        