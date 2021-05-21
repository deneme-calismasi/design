from tkinter import *
from tkcalendar import Calendar

# Create Object
root = Tk()

# Add Calender
cal = Calendar(root, selectmode='day',
               year=2021, month=5,
               day=19)

cal.pack(pady=20)


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())


print(cal.get_date())

# Add Button and Label
Button(root, text="Get Date",
       command=grad_date).pack(pady=20)

date = Label(root, text="")
date.pack(pady=20)

# Excecute Tkinter
root.mainloop()
