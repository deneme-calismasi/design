from tkinter import *
from PIL import ImageTk, Image

root = Tk()

canvas = Canvas(root, width=300, height=300, bg='white')
canvas.pack()

img = ImageTk.PhotoImage(Image.open("eae.png"))
canvas.create_image(200, 200, image=img, state="normal")

root.mainloop()
