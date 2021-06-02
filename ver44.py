import tkinter as tk
from tkinter import ttk
from tkinter import Tk

"""root = tk.Tk()
root.title("Sensor's Temperatures °C")
root.geometry("500x780")
root.grid()"""

root = tk.Tk()
tree = ttk.Treeview(root, displaycolumns='#all')
tree["columns"] = ("1", "2", "3", "4")
tree.column("#0", width=70)
tree.column("1", width=70, anchor=tk.CENTER)
tree.column("2", width=50, anchor=tk.CENTER)
tree.column("3", width=50, anchor=tk.CENTER)
tree.column("4", width=70, anchor=tk.CENTER)
tree.heading("1", text="Column 1")
tree.heading("2", text="Column 2")
tree.heading("3", text="Column 3")
tree.heading("4", text="Column 4")
id2 = []
count = 0
item_list = ['A', 'B', 'C', 'D']
for item in item_list:
    id = tree.insert("", count, iid='Row %s' % count, text=item, values=('1', '2', '3', '4'))
    id2.append(id)
    count += 1

tree.selection_set('Row 0')  # Doesn't work -- returns "_tkinter.TclError:  Item Row not found"
tree.pack(fill=tk.BOTH, expand=1, side=tk.RIGHT, padx=50)

tk.mainloop()
