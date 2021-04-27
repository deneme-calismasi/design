import random
import string
import tkinter as tk
from tkinter import ttk
from tkinter import *
from pandas import DataFrame
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def get_random_number():
    return random.uniform(1, 160)


def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str


data = [
    [1, get_random_string(3), round(get_random_number(), 2)],
    [2, get_random_string(3), round(get_random_number(), 2)],
    [3, get_random_string(3), round(get_random_number(), 2)],
    [4, get_random_string(3), round(get_random_number(), 2)],
    [5, get_random_string(3), round(get_random_number(), 2)],
    [6, get_random_string(3), round(get_random_number(), 2)],
    [7, get_random_string(3), round(get_random_number(), 2)],
    [8, get_random_string(3), round(get_random_number(), 2)],
    [9, get_random_string(3), round(get_random_number(), 2)],
    [10, get_random_string(3), round(get_random_number(), 2)],
    [11, get_random_string(3), round(get_random_number(), 2)],
    [12, get_random_string(3), round(get_random_number(), 2)],
    [13, get_random_string(3), round(get_random_number(), 2)],
    [14, get_random_string(3), round(get_random_number(), 2)],
    [15, get_random_string(3), round(get_random_number(), 2)],
]

data1 = {'Machine': [data[0][1], data[1][1], data[2][1], data[3][1], data[4][1], data[5][1], data[6][1], data[7][1],
                     data[8][1], data[9][1], data[10][1], data[11][1], data[12][1], data[13][1], data[14][1]],
         'Temperature': [data[0][2], data[1][2], data[2][2], data[3][2], data[4][2], data[5][2], data[6][2], data[7][2],
                         data[8][2], data[9][2], data[10][2], data[11][2], data[12][2], data[13][2], data[14][2]]
         }
df1 = DataFrame(data1, columns=['Machine', 'Temperature'])

data2 = {'Machine': [data[0][1], data[1][1], data[2][1], data[3][1], data[4][1], data[5][1], data[6][1], data[7][1],
                     data[8][1], data[9][1], data[10][1], data[11][1], data[12][1], data[13][1], data[14][1]],
         'Temperature': [data[0][2], data[1][2], data[2][2], data[3][2], data[4][2], data[5][2], data[6][2], data[7][2],
                         data[8][2], data[9][2], data[10][2], data[11][2], data[12][2], data[13][2], data[14][2]]
         }
df2 = DataFrame(data2, columns=['Machine', 'Temperature'])

root = tk.Tk()
root.title("Machine's Temperatures")
root.grid()

figure1 = plt.figure()
plt.style.use('fivethirtyeight')
ax = figure1.add_subplot(1, 1, 1)
xs = []
ys = []


# bar1 = FigureCanvasTkAgg(figure1, root)
# bar1.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)


def animate(i, xs, ys):
    # Read temperature (Celsius) from TMP102
    temp_c = round(get_random_number(), 2)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, linestyle='--')

    # Format plot
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

# Creating tkinter window

# root.resizable(width=1, height=1)

# Using treeview widget
# treev = ttk.Treeview(root, selectmode='browse')
treev = ttk.Treeview(root)

# Calling pack method w.r.to treeview
treev.pack(side='left', fill=tkinter.BOTH)

# Constructing vertical scrollbar
# with treeview
verscrlbar = ttk.Scrollbar(root,
                           orient="vertical",
                           command=treev.yview)

# Calling pack method w.r.to verical
# scrollbar
# verscrlbar.pack(side='top', fill='x', anchor=NW)

# Configuring treeview
treev.configure(xscrollcommand=verscrlbar.set)

# Defining number of columns
treev["columns"] = ("1", "2", "3")

# Defining heading
treev['show'] = 'headings'

# Assigning the width and anchor to  the
# respective columns
treev.column("1", width=40, minwidth=30, anchor='c')
treev.column("2", width=120, minwidth=30, anchor='c')
treev.column("3", width=120, minwidth=30, anchor='c')

# Assigning the heading names to the
# respective columns
treev.heading("1", text="ID")
treev.heading("2", text="Machine")
treev.heading("3", text="Temperature")

count = 0
for record in data:
    treev.insert("", index='end', iid=count, values=(record[0], record[1], record[2]))
    count += 1

treev = ttk.Style()
treev.configure('Treeview', rowheight=30)


def _quit():
    root.quit()  # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


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

'''
ip = Label(root, text="TCP/IP").place(x=10, y=10)
e1 = Entry(root).place(x=60, y=10)
host = Label(root, text=" PORT").place(x=10, y=40)
e2 = Entry(root).place(x=60, y=40)
submit = Button(root, text="Connect").place(x=40, y=70)
'''

# tkinter.mainloop()

root.mainloop()
