from tkinter import *


def toggle(canvas, items):
    if len(items) > 0:
        canvas.itemconfigure(items[0], fill="red")
        print(items)
        canvas.after(1000, lambda: toggle(canvas, items[1:]))
    return


root = Tk()
canvas = Canvas(root, width=1600, height=600)
canvas.pack()

x1 = 10
x2 = 1580
y1 = 150
y2 = 170
z1 = 500
z2 = 520
t1 = 365
t2 = 385

shape1 = canvas.create_rectangle(x1, y1, x2, y2, fill='grey', outline='white')
shape2 = canvas.create_rectangle(x1, z1, x2, z2, fill='grey', outline='white')
shape3 = canvas.create_rectangle(t1, y2, t2, z1, fill='grey', outline='white')


# canvas.after(1000, lambda: toggle(canvas, [shape4, shape5, shape6]))


def make():
    start1 = 40
    for x in range(26):
        shape4 = canvas.create_rectangle(start1, y1, start1 + 10, y2, fill='blue', outline='white', stipple='gray50')
        shape5 = canvas.create_rectangle(start1, z1, start1 + 10, z2, fill='blue', outline='white', stipple='gray50')
        start1 += 60

    start2 = 190
    for y in range(8):
        shape6 = canvas.create_rectangle(t1, start2, t2, start2 + 10, fill='blue', outline='white', stipple='gray50')
        start2 += 40
    root.after(1000, unmake)


def unmake():
    canvas.delete(ALL)
    shape1 = canvas.create_rectangle(x1, y1, x2, y2, fill='grey', outline='white')
    shape2 = canvas.create_rectangle(x1, z1, x2, z2, fill='grey', outline='white')
    shape3 = canvas.create_rectangle(t1, y2, t2, z1, fill='grey', outline='white')
    start3 = 45
    n = 1
    for z in range(26):
        canvas.create_text(start3, 140, text=n)
        canvas.create_text(start3, 530, text=n + 34)
        start3 += 60
        n += 1

    start4 = 195
    f = 27
    for t in range(8):
        canvas.create_text(395, start4, text=f)
        start4 += 40
        f += 1
    root.after(1000, make)


make()
root.mainloop()
