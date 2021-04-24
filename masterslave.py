from tkinter import *

root = Tk()
v = IntVar()
w = Label(root, text=" -Master/Slave- ")
w.grid(row=0, column=0)
Radiobutton(root, text='Master', variable=v, value=1).grid(row=1, column=0)
Radiobutton(root, text='Slave', variable=v, value=2).grid(row=2, column=0)

Label(root, text='Poll Time').grid(row=3)
Label(root, text='Response Time').grid(row=5)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=4, column=0)
e2.grid(row=6, column=0)

w = Label(root, text=" -Communications Mode- ")
w.grid(row=0, column=9)

Radiobutton(root, text='ASCII         ', variable=v, value=3).grid(row=1, column=9)
Radiobutton(root, text='Binary/RTU', variable=v, value=4).grid(row=2, column=9)

Radiobutton(root, text='TCP/IP     ', variable=v, value=5).grid(row=9, column=9)

Label(root, text='COM Port').grid(row=3, column=9)
w = Spinbox(root, from_=0, to=10)
w.grid(row=3, column=10)
Label(root, text='BaudRate').grid(row=4, column=9)
w = Spinbox(root, from_=0, to=10)
w.grid(row=4, column=10)
Label(root, text='Data Bits').grid(row=5, column=9)
w = Spinbox(root, from_=0, to=10)
w.grid(row=5, column=10)
Label(root, text='Parity').grid(row=6, column=9)
w = Spinbox(root, from_=0, to=10)
w.grid(row=6, column=10)
Label(root, text='Stop Bits').grid(row=7, column=9)
w = Spinbox(root, from_=0, to=10)
w.grid(row=7, column=10)

Label(root, text='IP Address').grid(row=10, column=9)
Label(root, text='Port').grid(row=11, column=9)
e3 = Entry(root)
e4 = Entry(root)
e3.grid(row=10, column=10)
e4.grid(row=11, column=10)

w = Label(root, text=" -ModBus- ")
w.grid(row=0, column=13)

w = Label(root, text="    Address")
w.grid(row=1, column=13)

Radiobutton(root, text='', variable=v, value=6).grid(row=2, column=13)
Radiobutton(root, text='', variable=v, value=7).grid(row=3, column=13)
Radiobutton(root, text='', variable=v, value=8).grid(row=4, column=13)
Radiobutton(root, text='', variable=v, value=9).grid(row=5, column=13)
Radiobutton(root, text='', variable=v, value=10).grid(row=6, column=13)


e5 = Entry(root)
e6 = Entry(root)
e7 = Entry(root)
e8 = Entry(root)
e9 = Entry(root)
e5.grid(row=2, column=14)
e6.grid(row=3, column=14)
e7.grid(row=4, column=14)
e8.grid(row=5, column=14)
e9.grid(row=6, column=14)

var1 = IntVar()
Checkbutton(root, text='Function 6 For Single Registers', variable=var1).grid(row=9, column=14)


root.mainloop()
