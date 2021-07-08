from tkinter import *

master = Tk()


def box_after(event):
    box = event.widget.find_closest(event.x, event.y)
    print(box)  # remove later
    w.itemconfig(box, fill='red')


def rowgen(row, col):
    for i in range(row):
        for j in range(col):
            w.create_rectangle(25 + 50 * i, 25 + 50 * j, 50 + 50 * i, 50 + 50 * j,
                               fill="green", tag='BOX')


w = Canvas(master, width=225, height=225)
w.pack()
rowgen(4, 4)
w.tag_bind('BOX', '<Button-1>', box_after)

master.resizable(0, 0)
mainloop()
