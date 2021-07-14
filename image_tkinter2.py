import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

photo = ImageTk.PhotoImage(Image.open('eae.png'))
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()
