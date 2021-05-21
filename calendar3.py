import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


# function to get value
def get_value():
    print(cal.get_date())


root = tk.Tk()
root.title("Date Picker")
s = ttk.Style(root)
s.theme_use('clam')

ttk.Label(root, text='Choose date').pack(padx=10, pady=10)

cal = DateEntry(root, width=12, background='darkblue',
                foreground='white', borderwidth=2)
cal.pack(padx=10, pady=10)

ttk.Button(root, width=10, text="Get Value", command=get_value).pack(padx=10, pady=10)

root.mainloop()
