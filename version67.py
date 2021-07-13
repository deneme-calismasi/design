import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter
import numpy as np
from pyModbusTCP.client import ModbusClient
import pymongo
import datetime as dt
import plotly.express as px
import pandas as pd

start_regs = 120
regs = [16877, 1455, 16880, 14214, 16881, 9306, 16879, 23690, 16880, 23901, 16876, 45600, 16861, 4767, 16858, 29102,
        16868, 22300, 16852, 764, 16856, 60158, 16859, 21030, 16855, 55104, 16856, 34289, 16853, 1282, 16856, 52178,
        16856, 55161, 16854, 44777, 16842, 23785, 16846, 14601, 16848, 45049, 16848, 23019, 16842, 15989, 16847, 41966,
        16847, 40499, 16852, 2953, 16841, 10119, 16852, 36451, 16851, 65201, 16846, 3452, 16852, 31945, 16845, 51201,
        16848, 44093, 16850, 16220, 16851, 29427, 16840, 40531, 16848, 23485, 16847, 38102, 16849, 19506, 16844, 3420,
        16846, 9849, 16841, 47197, 16836, 63407, 16834, 36692, 16841, 24711, 16840, 22376, 16840, 54442, 16833, 32311,
        16838, 16202, 16835, 33673, 16837, 27663, 16836, 61659, 16834, 12204, 16832, 53624, 16835, 2459, 16838, 37479,
        16830, 12750, 16832, 52962, 16835, 26281, 16840, 14599]

for n in range(start_regs // 2):
    data_count = n * 2
    regs[data_count], regs[data_count + 1] = regs[data_count + 1], regs[data_count]

dec_array = regs

data_bytes = np.array(dec_array, dtype=np.uint16)
data_as_float = data_bytes.view(dtype=np.float32)

time_data = dt.datetime.now().strftime('%Y-%m-%d %X')

start = 1
start_range = start_regs // 2

value = [[num for num in range(start, start + start_range)],
         [num for num in range(start, start + start_range)],
         data_as_float]

data = np.array(value).T.tolist()

products = data
arr = []
for product in products:
    vals = {}
    vals["Sensor No"] = str(int(product[1]))
    vals["Temp"] = str(round(product[2], 4))
    vals["Time"] = str(time_data)
    arr.append(vals)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Modbus_Database"]

mycol = mydb["collection1"]

record_data = arr
mycol.insert_many(record_data)

documents = list(mycol.find({}, {'_id': 0}))
res = [list(idx.values()) for idx in documents]

for index1, row in enumerate(res):
    for index2, item in enumerate(row):
        try:
            res[index1][index2] = (float(item))
        except ValueError:
            pass


def on_double_click(event):
    item = tree.identify('item', event.x, event.y)
    print(tree.item(item, "text"))

    xs_doc = list(
        mycol.find(
            {"$and": [{"Sensor No": tree.item(item, "text")},
                      {"Time": {"$gte": "2021-05-31 13:14:58", "$lt": time_data}}]},
            {'_id': 0}))

    xs_res = [list(idx.values()) for idx in xs_doc]

    for index1, row in enumerate(xs_res):
        for index2, item in enumerate(row):
            try:
                xs_res[index1][index2] = (float(item))
            except ValueError:
                pass

    df = pd.DataFrame(xs_doc)
    df['Temp'] = df['Temp'].astype(np.float64)
    fig = px.line(df, x='Time', y='Temp', title='Temperature °C - Time', color='Sensor No')

    fig.update_xaxes(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=3, label="3m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    fig.show()


myquery = {"Time": {"$gte": "2021-05-31 13:14:58", "$lt": time_data}}
mydoc = mycol.find(myquery)

mydoc_all = mycol.find()
df = pd.DataFrame(list(mydoc_all))
df['Temp'] = df['Temp'].astype(np.float64)

root = tk.Tk()
root.title("Sensor's Temperatures °C")
root.geometry()
root.grid()

p1 = PhotoImage(file='../modbusOOP/images1.png')
root.iconphoto(False, p1)

tree = ttk.Treeview(root)

tree.pack(side='top', fill=tkinter.BOTH, expand=True)

verscrlbar = ttk.Scrollbar(root,
                           orient="vertical",
                           command=tree.yview)

tree.configure(xscrollcommand=verscrlbar.set)

tree["columns"] = ("1", "2", "3", "4")

tree['show'] = 'headings'

tree.column("1", width=115, minwidth=30, anchor='c')
tree.column("2", width=125, minwidth=30, anchor='c')
tree.column("3", width=65, minwidth=30, anchor='c')
tree.column("4", width=115, minwidth=30, anchor='c')

tree.heading("1", text="ID")
tree.heading("2", text="Time")
tree.heading("3", text="Sensor No")
tree.heading("4", text="Temperature °C")

tree.bind("<Double-1>", on_double_click)


def _quit():
    root.quit()
    root.destroy()


# Add a canvas inside the frame
canvas = Canvas(root, width=1600, height=600)
canvas.pack()

# Add a rectangle inside the canvas widget
shape1 = canvas.create_rectangle(10, 150, 1580, 170, fill='grey', outline='white')
shape2 = canvas.create_rectangle(10, 500, 1580, 520, fill='grey', outline='white')
shape3 = canvas.create_rectangle(365, 170, 385, 500, fill='grey', outline='white')

start3 = 45
n = 1
for z in range(26):
    canvas.create_text(start3, 140, text=n)
    canvas.create_text(start3, 530, text=n + 34)
    start3 += 60
    n += 1

start4 = 195
f = 27
for t in range(8):
    canvas.create_text(395, start4, text=f)
    start4 += 40
    f += 1


def create_ver(start, y_lower, y_upper, color):
    pass


def create_hor(start, x_lower, x_upper, color):
    pass


start_range = 0
id_count = 1
start = 40

for record in res[-(start_regs // 2):]:
    sensor_id = record[0]
    temperature = record[1]
    date_time = record[2]
    tree.insert("", index='end', text="%s" % int(record[0]), iid=start_range,
                values=(int(id_count), str(record[2]), int(record[0]), float(record[1])))

    if record[0] <= 26.0:
        # ust cizgi

        x_to_add = 60
        y_lower, y_upper = 150, 170
        if float(record[1]) > 25.0:
            shape4 = canvas.create_rectangle(start, y_lower, start + 10, y_upper, fill='red', outline='white',
                                             stipple='gray50')

        else:
            shape4 = canvas.create_rectangle(start, y_lower, start + 10, y_upper, fill='blue', outline='white',
                                             stipple='gray50')
        start += x_to_add

        if record[0] == 26:
            start = 190

    elif 26.0 < record[0] < 35.0:
        y_to_add = 40
        x_lower, x_upper = 365, 385
        if float(record[1]) > 25.0:
            shape6 = canvas.create_rectangle(x_lower, start, x_upper, start + 10, fill='red', outline='white',
                                             stipple='gray50')
        else:
            shape6 = canvas.create_rectangle(x_lower, start, x_upper, start + 10, fill='blue', outline='white',
                                             stipple='gray50')
        start += y_to_add
        if record[0] == 34:
            start = 40
    else:
        # alt cizgi
        x_to_add = 60
        y_lower, y_upper = 500, 520
        if float(record[1]) > 25:
            shape5 = canvas.create_rectangle(start, y_lower, start + 10, y_upper, fill='red', outline='white',
                                             stipple='gray50')
        else:
            shape5 = canvas.create_rectangle(start, y_lower, start + 10, y_upper, fill='blue', outline='white',
                                             stipple='gray50')
        start += x_to_add

    start_range += 1
    id_count += 1

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open Calendar')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=_quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Figure')
helpmenu.add_command(label='About')

if __name__ == '__main__':
    root.mainloop()
