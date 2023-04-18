# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 01:10:55 2023

@author: Korisnik
"""

import tkinter as tk

def calculate_npv():
    cashflows = [float(c) for c in cashflow_entry.get().split(',')]
    investment = float(investment_entry.get())
    rate = float(rate_entry.get())
    npv = investment + sum([cf / (1 + rate) ** i for i, cf in enumerate(cashflows)])
    result_label.config(text=f"Net Present Value: {npv}")

root = tk.Tk()
root.title("NPV Calculator")

investment_label = tk.Label(root, text="Investment:")
investment_label.grid(row=0, column=0)

investment_entry = tk.Entry(root)
investment_entry.grid(row=0, column=1)

cashflow_label = tk.Label(root, text="Cash Flows:")
cashflow_label.grid(row=1, column=0)

cashflow_entry = tk.Entry(root)
cashflow_entry.grid(row=1, column=1)

rate_label = tk.Label(root, text="Discount Rate:")
rate_label.grid(row=2, column=0)

rate_entry = tk.Entry(root)
rate_entry.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate NPV", command=calculate_npv)
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()