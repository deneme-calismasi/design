from tkinter import *

canvas = Canvas(width=300, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)

canvas.create_oval(1250, 625, 1500, 875, width=2, fill='blue')

mainloop()
