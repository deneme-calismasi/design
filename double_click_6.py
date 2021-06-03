import tkinter as tk
from tkinter import ttk


def on_double_click(event):
    item_id = event.widget.focus()
    item = event.widget.item(item_id)
    values = item['values']
    url = values[0]
    print(url)


root = tk.Tk()
t = ttk.Treeview(root)
t.pack(fill="both", expand=True)

t.bind("<Double-Button-1>", on_double_click)

for x in range(10):
    url = "%d" % x
    text = "item %d" % x
    t.insert("", x, text=text, values=[url])

root.mainloop()
