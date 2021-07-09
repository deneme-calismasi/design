from tkinter import *

root = Tk()
canvas = Canvas(root)
canvas.pack()
canvas.create_rectangle(0, 0, 100, 100, fill='red', tag='rect')


def task():
    l = root.after(1000, task)
    if int(l.split('#')[1]) % 2 == 0:
        canvas.itemconfig('rect', fill='blue')
    else:
        canvas.itemconfig('rect', fill='red')


task()

root.mainloop()
