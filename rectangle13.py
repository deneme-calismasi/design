from tkinter import *

root = Tk()
root.title("pyChess")
# window.geometry("523x523+250+0")
# window.configure(background='grey')

x1 = 0
y1 = 0
x2 = 65
y2 = 65
j1 = 65
k1 = 0
j2 = 130
k2 = 65
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for x, shape in enumerate(a):
    shape = Canvas(root, width=130, height=65)
    shape.create_rectangle(0, 0, 65, 65, fill="red")
    shape.create_rectangle(65, 0, 130, 65, fill="blue")
    shape.grid(row=0, column=x)

root.mainloop()
