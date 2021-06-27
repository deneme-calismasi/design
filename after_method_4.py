import tkinter as tk


def delay_and_print():
    global number
    if number < 50:
        print(number)
        label.config(text=number)
        number += 1
        root.after(3000, delay_and_print)


root = tk.Tk()
number = 0
tk.Button(root, text='Start', command=delay_and_print).pack()
label = tk.Label(root, text='')
label.pack()
root.mainloop()
