import tkinter as tk
from datetime import date
import requests 

class DateButton:
    def __init__(self, root):
        self.root = root
        self.date_button = tk.Button(self.root, text=f"{date.today()}", font=("Menlo", 18, "bold"), command=self.show_date)
        self.date_button.grid(row=0, columnspan=5, sticky="nsew")

    def show_date(self):
        response = requests.get('https://www.hebcal.com/converter?cfg=json&gy={year}&gm={month}&gd={day}&g2h=1'.format(year=date.today().year, month=date.today().month, day=date.today().day))
        data = response.json()
        hebrew_date = data['hebrew']

        date_window = tk.Toplevel(self.root)
        date_window.title("Hebrew Date")

        tk.Label(date_window, text=f"Hebrew Date:\n {hebrew_date}", font=("Menlo", 26, "bold")).pack(padx=80,pady=50)   
    