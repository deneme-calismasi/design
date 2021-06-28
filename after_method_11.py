from random import randint
from tkinter import ttk
from tkinter import *

root = Tk()

tree = ttk.Treeview(root)


def update():
    mpb["value"] = randint(0, 100)  # take process bar for example
    root.after(1000, update)


update()
root.mainloop()
