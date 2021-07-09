from tkinter import *

root = Tk()
root.title("pyChess")
canvas = Canvas(root)
canvas.pack()

bs = 20
x_values = ['3', '4', '5', '6']
y_values = ['5', '5', '5', '5']

for x1, y1 in zip(x_values, y_values):
    x1 = int(x1) * bs
    y1 = int(y1) * bs
    x2 = x1 + bs
    y2 = y1 + bs
    canvas.create_rectangle(x1, y1, x2, y2, fill="red")

root.mainloop()
