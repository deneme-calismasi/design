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
sensor_no = ModbusClient(host="192.40.50.107", port=10010, unit_id=1, auto_open=True)
sensor_no.open()
regs = sensor_no.read_holding_registers(0, start_regs)
if regs:
    print(regs)
else:
    print("read error")

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
# root.geometry("480x630")
root.geometry()
root.grid()

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

start2 = 190
for y in range(8):
    shape6 = canvas.create_rectangle(365, start2, 385, start2 + 10, fill='blue', outline='white', stipple='gray50')
    start2 += 40

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

start_range = 0
id_count = 1

for record in res[-(start_regs // 2):]:
    tree.insert("", index='end', text="%s" % int(record[0]), iid=start_range,
                values=(int(id_count), str(record[2]), int(record[0]), float(record[1])))
    start1 = 40
    for x in range(26):
        if float(record[1]) > 30.0:
            shape4 = canvas.create_rectangle(start1, 150, start1 + 10, 170, fill='red', outline='white',
                                             stipple='gray50')
            shape5 = canvas.create_rectangle(start1, 500, start1 + 10, 520, fill='red', outline='white',
                                             stipple='gray50')

        else:
            shape4 = canvas.create_rectangle(start1, 150, start1 + 10, 170, fill='blue', outline='white',
                                             stipple='gray50')
            shape5 = canvas.create_rectangle(start1, 500, start1 + 10, 520, fill='blue', outline='white',
                                             stipple='gray50')
        start1 += 60

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
