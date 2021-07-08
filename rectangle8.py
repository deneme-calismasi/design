from tkinter import *

window = Tk()
window.title("pyChess")
window.geometry("523x523+250+0")
window.configure(background='grey')

x1 = 0
y1 = 0
x2 = 65
y2 = 65
j1 = 65
k1 = 0
j2 = 130
k2 = 65
a = [0, 1, 2, 3, 4, 5, 6]

for x, i in enumerate(a):
    i = Canvas(window, width=130, height=65)
    i.create_rectangle(x1, y1, x2, y2, fill="white")
    i.create_rectangle(j1, k1, j2, k2, fill="black")
    i.grid(row=0, column=x)

window.mainloop()
