from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button

from time import time

base = Tk()

stud = Button(base, text='After Demo()')
stud.pack(side=TOP, pady=8)

print('processing Begins...')

begin = time()

base.after(3000, base.destroy)

mainloop()

conclusion = time()
print('process destroyed in % d seconds' % (conclusion - begin))
