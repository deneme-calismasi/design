import string
import tkinter as tk
from tkinter import ttk
from tkinter import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random


def get_random_number():
    return random.uniform(1, 180)


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
# root.geometry("1200x1200")

figure1 = plt.Figure(figsize=(4, 4), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
df1 = df1[['Machine', 'Temperature']].groupby('Machine').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Machine Vs. Temperature')

figure2 = plt.Figure(figsize=(4, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
df2 = df2[['Machine', 'Temperature']].groupby('Machine').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
ax2.set_title('Machine Vs. Temperature')

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

w = Label(root, text="Machine's Temperatures")
w.pack()

# Creating tkinter window

# root.resizable(width=1, height=1)

# Using treeview widget
# treev = ttk.Treeview(root, selectmode='browse')
treev = ttk.Treeview(root)

# Calling pack method w.r.to treeview
treev.pack(side='left')

# Constructing vertical scrollbar
# with treeview
verscrlbar = ttk.Scrollbar(root,
                           orient="vertical",
                           command=treev.yview)

# Calling pack method w.r.to verical
# scrollbar
verscrlbar.pack(side='left', fill='x')

# Configuring treeview
treev.configure(xscrollcommand=verscrlbar.set)

# Defining number of columns
treev["columns"] = ("1", "2", "3")

# Defining heading
treev['show'] = 'headings'

# Assigning the width and anchor to  the
# respective columns
treev.column("1", width=60, minwidth=40, anchor='c')
treev.column("2", width=160, minwidth=40, anchor='c')
treev.column("3", width=160, minwidth=40, anchor='c')

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
treev.configure('Treeview', rowheight=40)

root.mainloop()
