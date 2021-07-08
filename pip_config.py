from tkinter import *


def toggle(canvas, items):
    if len(items) > 0:
        canvas.itemconfigure(items[0], fill="green")
        canvas.after(1000, lambda: toggle(canvas, items[1:]))
    return


root = Tk()
canvas = Canvas(root, background="white")
canvas.pack(fill='both', expand=True)
figure1 = canvas.create_rectangle(10, 10, 80, 80, fill="red")
figure2 = canvas.create_rectangle(100, 10, 180, 80, fill="red")
figure3 = canvas.create_rectangle(200, 10, 280, 80, fill="red")
canvas.after(1000, lambda: toggle(canvas, [figure1, figure2, figure3]))
root.mainloop()
