import tkinter as tk
from tkinter import *
from pandas import DataFrame
from pandastable import Table
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

randomlist3 = random.sample(range(1500, 1565), 10)

randomlist4 = random.sample(range(1500, 1565), 10)

data3 = {'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
         'Stock_Index_Price': randomlist3
         }
df3 = DataFrame(data3, columns=['Interest_Rate', 'Stock_Index_Price'])

data4 = {'Interest_Rate': [4, 4.5, 5, 5.5, 6.25, 6.5, 7, 8, 7.5, 8.5],
         'Stock_Index_Price': randomlist4
         }

df4 = DataFrame(data4, columns=['Interest_Rate', 'Stock_Index_Price'])

root = tk.Tk()
root.title("test it is")
root.grid()

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, ],
    'B': [1, 1, 2, 2, 3, 3, ],
    'C': [1, 2, 3, 1, 2, 3, ],
    'D': [1, 1, 1, 2, 2, 2, ],
})

root.title('PandasTable Example')

frame = tk.Frame(root)
frame.pack(side=tk.TOP, fill=tk.BOTH)

pt = Table(frame, showtoolbar=True, showstatusbar=True)
# pt = Table(frame, dataframe=df)
pt.show()

pt.columncolors['A'] = 'red'
pt.columncolors['B'] = 'green'

figure3 = plt.Figure(figsize=(5, 4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Interest_Rate'], df3['Stock_Index_Price'], color='g')
ax3.scatter(df4['Interest_Rate'], df4['Stock_Index_Price'], color='b')
scatter3 = FigureCanvasTkAgg(figure3, root)
scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax3.legend(['Stock_Index_Price'])
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Stock Index Price')




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
