import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

photo = ImageTk.PhotoImage(Image.open('elec.png'))
label = tk.Label(root, image=photo, text='east')
label.place(relx=0.95, rely=0.75, anchor='e')
# label.pack()

root.mainloop()
