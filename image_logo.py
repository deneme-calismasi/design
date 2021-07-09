# Importing Tkinter module
from tkinter import *
from tkinter.ttk import *

# Creating master Tkinter window
root = Tk()

# Creating object of photoimage class
# Image should be in the same folder
# in which script is saved
p1 = PhotoImage(file='../modbusOOP/images1.png')

# Setting icon of master window
root.iconphoto(False, p1)

# Creating button
b = Button(root, text='Click me !')
b.pack(side=TOP)

# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
root.mainloop()
