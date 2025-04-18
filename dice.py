import tkinter as tk
import random as rand

window = tk.Tk()
window.title("Dice Roll")

window.rowconfigure([0,1], minsize=70, weight=1)
window.columnconfigure(0, minsize=25, weight=1)

def dice_roll():
    lbl_value["text"] = f"{rand.randint(1,6)}"


lbl_value = tk.Label(master=window, text="")
lbl_value.grid(row=1,column=0)

btn_roll = tk.Button(master=window, text="Roll", command=dice_roll)
btn_roll.grid(row=0,column=0,sticky="nsew")

window.mainloop()