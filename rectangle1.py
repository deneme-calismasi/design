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
shape1 = canvas.create_rectangle(10, 150, 1580, 170, fill='grey', outline='white')
shape2 = canvas.create_rectangle(10, 500, 1580, 520, fill='grey', outline='white')
shape3 = canvas.create_rectangle(365, 170, 385, 500, fill='grey', outline='white')
canvas.after(1000, lambda: toggle(canvas, [shape4, shape5, shape6]))

start1 = 40
for x in range(26):
    shape4 = canvas.create_rectangle(start1, 150, start1 + 10, 170, fill='blue', outline='white', stipple='gray50')
    shape5 = canvas.create_rectangle(start1, 500, start1 + 10, 520, fill='blue', outline='white', stipple='gray50')
    start1 += 60

start2 = 190
for y in range(8):
    shape6 = canvas.create_rectangle(365, start2, 385, start2 + 10, fill='blue', outline='white', stipple='gray50')
    start2 += 40

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
root.mainloop()
