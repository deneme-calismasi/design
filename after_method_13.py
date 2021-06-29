# importing only those functions which
# are needed
from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
from tkinter.messagebox import _show

# creating tkinter window
root = Tk()
root.geometry('200x100')

button = Button(root, text='Geeks')
button.pack(side=TOP, pady=5)

# in after method 5000 milliseconds
# is passed i.e after 5 seconds
# a message will be prompted
root.after(5000, lambda: _show('Title', 'Prompting after 5 seconds'))

# Destroying root window after 6.7 seconds
root.after(6700, root.destroy)

mainloop()
