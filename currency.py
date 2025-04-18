import tkinter as tk
from tkinter import ttk


rates = {
    "USD": 1.0,
    "EUR": 0.93,
    "GBP": 0.80,
    "ALL": 95.75
}

def convert():
    try:
        amount = float(ent_amount.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        result = amount * rates[to_curr] / rates[from_curr]
        result_label.config(text= f"{amount:.2f} {from_curr} = {result: .2f} {to_curr}")
    except:
        result_label.config(text="Invalid input")

window = tk.Tk()
window.title("Currency Converter")
window.resizable(height=False, width=False)


tk.Label(text="Amount: ").pack(pady=5)
ent_amount = tk.Entry(window)
ent_amount.pack()

tk.Label(window,text="From: ").pack(pady=5)
from_currency = ttk.Combobox(window,values=list(rates.keys()),state="readonly")
from_currency.set("USD")
from_currency.pack(padx=5)

tk.Label(window, text="To:").pack(pady=5)
to_currency = ttk.Combobox(window,values=list(rates.keys()),state="readonly")
to_currency.set("EUR")
to_currency.pack(padx=5)

tk.Button(window,text="Convert", command=convert).pack(pady=10)

result_label = tk.Label(window,text="Result will show here")
result_label.pack(pady=10)

window.mainloop()