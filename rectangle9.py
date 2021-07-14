from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)

canvas.create_oval(1250, 625, 1500, 875, fill='blue', tag='circle')


def task():
    circle = root.after(500, task)
    if int(circle.split('#')[1]) % 2 == 0:
        canvas.itemconfig('circle', fill='blue')
    else:
        canvas.itemconfig('circle', fill='red')


task()

root.mainloop()
