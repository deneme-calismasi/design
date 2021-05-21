from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

root = Tk()

e7 = DateEntry(root, values="Text", year=2021, state="readonly", date_pattern="yyyy/mm/dd")
e7.grid(row=1, column=1, padx=20, pady=5, sticky=W)

root.mainloop()
