import tkinter as tk

window = tk.Tk()
window.title("Adress Entry Form")

frm_form = tk.Frame(master=window, relief='sunken',borderwidth=3)
frm_form.pack()

labels = [
    "First Name:",
    "Last Name:",
    "Address:",
    "City",
    "Postal Code:",
    "Country:"
]

for idx,text in enumerate(labels):
    label = tk.Label(master=frm_form, text=text)
    entry = tk.Entry(master=frm_form, width=50)

    label.grid(row=idx,column=0,sticky="e")
    entry.grid(row=idx, column=1)

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5,ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()