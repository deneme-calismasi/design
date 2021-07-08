from tkinter import *

root = Tk()


def make():
    canvas.create_rectangle(20, 20, 60, 60, fill="pink")
    root.after(1000, unmake)


def unmake():
    canvas.delete(ALL)
    root.after(1000, make)


canvas = Canvas(root, width=100, height=100)
canvas.pack()

make()

root.mainloop()
