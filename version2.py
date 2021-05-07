import string
import tkinter as tk
from tkinter import ttk
from tkinter import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

randomlist = random.sample(range(1000, 1500), 10)

randomlist2 = random.sample(range(1000, 1500), 10)

randomlist3 = random.sample(range(1500, 1565), 10)

randomlist4 = random.sample(range(1500, 1565), 10)


def get_number_generator():
    return random.uniform(1, 180)


def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str


x = get_random_string(5)
y = get_random_string(5)
z = get_random_string(5)
t = get_random_string(5)
u = get_random_string(5)

a = round(get_number_generator(), 2)
b = round(get_number_generator(), 2)
c = round(get_number_generator(), 2)
d = round(get_number_generator(), 2)
e = round(get_number_generator(), 2)

data1 = {'Machine': [x, y, z, t, u],
         'Temperature': [a, b, c, d, e]
         }
df1 = DataFrame(data1, columns=['Machine', 'Temperature'])

data3 = {'Temperature': randomlist,
         'Temperature': randomlist3
         }
df3 = DataFrame(data3, columns=['Interest_Rate', 'Temperature'])

data4 = {'Machine': randomlist2,
         'Temperature': randomlist4
         }

df4 = DataFrame(data4, columns=['Machine', 'Temperature'])

root = tk.Tk()
root.title("Machine's Temperatures")
root.grid()
# root.geometry("600x900")

figure1 = plt.Figure(figsize=(5, 4), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
df1 = df1[['Machine', 'Temperature']].groupby('Machine').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Machine Vs. Temperature')

"""
figure3 = plt.Figure(figsize=(5, 4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Interest_Rate'], df3['Stock_Index_Price'], color='g')
ax3.scatter(df4['Interest_Rate'], df4['Stock_Index_Price'], color='b')
scatter3 = FigureCanvasTkAgg(figure3, root)
scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax3.legend(['Stock_Index_Price'])
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Stock Index Price')
"""
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
treev["columns"] = ("1", "2", "3",)

# Defining heading
treev['show'] = 'headings'

# Assigning the width and anchor to  the
# respective columns
treev.column("1", width=120, minwidth=25, anchor='c')
treev.column("2", width=120, minwidth=25, anchor='c')
treev.column("3", width=120, minwidth=25, anchor='c')

# Assigning the heading names to the
# respective columns
treev.heading("1", text="ID")
treev.heading("2", text="Machine")
treev.heading("3", text="Temperature")

"""
# Inserting the items and their features to the
# columns built
treev.insert("", 'end', text="L1",
             values=("Nidhi", "F", "25"))
treev.insert("", 'end', text="L2",
             values=("Nisha", "F", "23"))
treev.insert("", 'end', text="L3",
             values=("Preeti", "F", "27"))
treev.insert("", 'end', text="L4",
             values=("Rahul", "M", "20"))
treev.insert("", 'end', text="L5",
             values=("Sonu", "F", "18"))
treev.insert("", 'end', text="L6",
             values=("Rohit", "M", "19"))
treev.insert("", 'end', text="L7",
             values=("Geeta", "F", "25"))
treev.insert("", 'end', text="L8",
             values=("Ankit", "M", "22"))
treev.insert("", 'end', text="L10",
             values=("Mukul", "F", "25"))
treev.insert("", 'end', text="L11",
             values=("Mohit", "M", "16"))
treev.insert("", 'end', text="L12",
             values=("Vivek", "M", "22"))
treev.insert("", 'end', text="L13",
             values=("Suman", "F", "30"))

"""
data = [
    [1, x, a],
    [2, y, b],
    [3, z, c],
    [4, t, d],
    [5, u, d],
]

count = 0
for record in data:
    treev.insert("", index='end', iid=count, values=(record[0], record[1], record[2]))
    count += 1

root.mainloop()
