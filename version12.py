import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from pyModbusTCP.client import ModbusClient

c = ModbusClient(host="192.40.50.107", port=10010, unit_id=1, auto_open=True)

c.open()

start = 1
count = 30

regs = c.read_holding_registers(0, count)
if regs:
    print(regs)
else:
    print("read error")


def get_random_number():
    return random.uniform(1, 160)


value = [[num for num in range(start, start + count)],
         [num for num in range(start, start + count)],
         regs]

data = np.array(value).T.tolist()
print(data)

root = tk.Tk()
root.title("Machine's Temperatures")
root.grid()

figure1 = plt.figure()
plt.style.use('fivethirtyeight')
ax = figure1.add_subplot(1, 1, 1)
xs = []
ys = []


def animate(i, xs, ys):
    a = 0
    for i in range(10):
        a += 1
        temp_c = round(get_random_number(), 2)
        xs.append(a)
        ys.append(temp_c)

    ax.clear()
    ax.plot(xs, ys, color='blue', marker='o', markerfacecolor='red')

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature over Time')
    plt.ylabel('Temperature (deg C)')


canvas = FigureCanvasTkAgg(figure1, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)

ani = animation.FuncAnimation(figure1, animate, fargs=(xs, ys), interval=1000)

treev = ttk.Treeview(root)

treev.pack(side='left', fill=tkinter.BOTH)

verscrlbar = ttk.Scrollbar(root,
                           orient="vertical",
                           command=treev.yview)

treev.configure(xscrollcommand=verscrlbar.set)

treev["columns"] = ("1", "2", "3")

treev['show'] = 'headings'

treev.column("1", width=40, minwidth=30, anchor='c')
treev.column("2", width=120, minwidth=30, anchor='c')
treev.column("3", width=120, minwidth=30, anchor='c')

treev.heading("1", text="ID")
treev.heading("2", text="Machine")
treev.heading("3", text="Temperature")

for record in data:
    treev.insert("", index='end', iid=count, values=(record[0], record[1], record[2]))
    count += 1

treev = ttk.Style()
treev.configure('Treeview', rowheight=30)


def _quit():
    root.quit()
    root.destroy()


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=_quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

ip = Label(root, text="TCP/IP").pack(side=TOP)
e1 = Entry(root).pack(side=TOP)
host = Label(root, text=" PORT").pack(side=TOP)
e2 = Entry(root).pack(side=TOP)
submit = Button(root, text="Connect").pack(side=TOP)

root.mainloop()
