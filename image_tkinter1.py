import tkinter
from tkinter import *

root = tkinter.Tk()
root.configure(background='#16e116')
root.title('Pop Up')
root.geometry('300x200')

photo = PhotoImage(file="eae.png")

w = Label(root, image=photo)
text = Label(root, text="Hello world!")

w.grid(row=300, column=300)
text.grid(row=3, column=3)

root.mainloop()
