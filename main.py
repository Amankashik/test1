print("hello World!")
#!/usr/bin/python3
import tkinter as tk

root = tk.Tk()

root.geometry("300x400")
btn_color="blue"
lbl_text="Tom's Calculator"

############################################################################################


top_frame = tk.Frame(root)
top_frame.grid(row=0, column=0, columnspan=4)
 
title_label = tk.Label(top_frame, text=lbl_text, font=("Arial", 16), bg="lightgray")
title_label.grid(row=0, column=0, columnspan=4, sticky="we")
entry = tk.Entry(top_frame, font=("Arial", 18), bd=5, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=1, column=0, columnspan=4, pady=10)
 
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

 
button_values = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

 
for i, row in enumerate(button_values):
    for j, value in enumerate(row):
        if value == "C":
            btn = tk.Button(root, text=value, padx=20, pady=20, font=("Arial", 14),
                            bg=btn_color, command=clear)
        elif value == "=":
            btn = tk.Button(root, text=value, padx=20, pady=20, font=("Arial", 14),
                            bg=btn_color, command=calculate)
        else:
            btn = tk.Button(root, text=value, padx=20, pady=20, font=("Arial", 14),
                            bg=btn_color, command=lambda v=value: button_click(v))
        btn.grid(row=i+2, column=j, padx=5, pady=5)

 
root.mainloop()
