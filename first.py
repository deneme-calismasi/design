import tkinter as tk
from tkinter import *
from pandas import DataFrame
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

figure3 = plt.Figure(figsize=(5, 4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Interest_Rate'], df3['Stock_Index_Price'], color='g')
ax3.scatter(df4['Interest_Rate'], df4['Stock_Index_Price'], color='b')
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

w = Label(root, text='GeeksForGeeks.org!')
w.pack()

Lb = Listbox(root)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(END, 'This is line number' + str(randomlist3))
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

root.mainloop()
