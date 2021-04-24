import tkinter as tk
from tkinter import *
from pandas import DataFrame
from pandastable import Table
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

randomlist = random.sample(range(10, 50), 10)

randomlist2 = random.sample(range(10, 100), 10)

randomlist3 = random.sample(range(1500, 1565), 10)

randomlist4 = random.sample(range(1500, 1565), 10)

randomlist5 = random.sample(range(1500, 1565), 10)

data1 = {'Country': ['USA', 'CA', 'GER', 'UK', 'FR', 'TR', 'SPA', 'ITA', 'BEL', 'AUS'],
         'GDP_Per_Capita': randomlist
         }
df1 = DataFrame(data1, columns=['Country', 'GDP_Per_Capita'])

data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
         'Unemployment_Rate': randomlist2
         }
df2 = DataFrame(data2, columns=['Year', 'Unemployment_Rate'])

data3 = {'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
         'Stock_Index_Price': randomlist3
         }
df3 = DataFrame(data3, columns=['Interest_Rate', 'Stock_Index_Price'])

data4 = {'Interest_Rate': [4, 4.5, 5, 5.5, 6.25, 6.5, 7, 8, 7.5, 8.5],
         'Stock_Index_Price': randomlist4
         }

df4 = DataFrame(data4, columns=['Interest_Rate', 'Stock_Index_Price'])

data5 = {'Interest_Rate': [4, 4.5, 5, 5.5, 6.25, 6.5, 7, 8, 7.5, 8.5],
         'Stock_Index_Price': randomlist5
         }

df5 = DataFrame(data5, columns=['Interest_Rate', 'Stock_Index_Price'])

root = tk.Tk()
root.title("test it is")
root.grid()

figure1 = plt.Figure(figsize=(5, 6), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
df1 = df1[['Country', 'GDP_Per_Capita']].groupby('Country').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')

figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
df2 = df2[['Year', 'Unemployment_Rate']].groupby('Year').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
ax2.set_title('Year Vs. Unemployment Rate')

figure3 = plt.Figure(figsize=(5, 4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Interest_Rate'], df3['Stock_Index_Price'], color='g')
ax3.scatter(df4['Interest_Rate'], df4['Stock_Index_Price'], color='b')
ax3.scatter(df5['Interest_Rate'], df5['Stock_Index_Price'], color='r')
scatter3 = FigureCanvasTkAgg(figure3, root)
scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax3.legend(['Stock_Index_Price'])
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Stock Index Price')








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
mainloop()

"""

def randnum(event):
    import random
    value = random.randint(1, 10)
    print(value)
    updateDisplay(value)

def updateDisplay(myString):
    displayVariable.set(myString)

button_1 = Button(root, text="test")
button_1.bind("<Button-1>", randnum)
button_1.pack()
displayVariable = StringVar()
displayLabel = Label(root, textvariable=displayVariable)
displayLabel.pack()

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)
left = Entry(m1, bd=5)
m1.add(left)
m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)
top = Scale(m2, orient=HORIZONTAL)
m2.add(top)



w = Scale(root, from_=0, to=42)
w.pack()
w = Scale(root, from_=0, to=200, orient=HORIZONTAL)
w.pack()

w = Spinbox(root, from_=0, to=10)
w.pack()




master = Tk()
w = Scale(master, from_=0, to=42)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
mainloop()

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()
"""

root.mainloop()
