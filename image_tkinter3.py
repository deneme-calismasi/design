from tkinter import *
from PIL import ImageTk, Image

root = Tk()

canvas = Canvas(root)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("../modbusOOP/elec.png"))
canvas.create_image((200, 200), image=img, state="normal")

root.mainloop()
