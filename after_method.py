import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter
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

root = tk.Tk()
root.title("Sensor's Temperatures °C")
root.geometry("480x630")
root.grid()

tree = ttk.Treeview(root)
tree.pack(side='top', fill=tkinter.BOTH, expand=True)

verscrlbar = ttk.Scrollbar(root,
                           orient="vertical",
                           command=tree.yview)

tree.configure(xscrollcommand=verscrlbar.set)

tree["columns"] = ("1", "2", "3")

tree['show'] = 'headings'

tree.column("1", width=125, minwidth=30, anchor='c')
tree.column("2", width=65, minwidth=30, anchor='c')
tree.column("3", width=115, minwidth=30, anchor='c')

tree.heading("1", text="Time")
tree.heading("2", text="Sensor No")
tree.heading("3", text="Temperature °C")

start_range = 0

for record in res[-(start_regs // 2):]:
    tree.insert("", index='end', text="%s" % int(record[0]), iid=start_range,
                values=(str(record[2]), int(record[0]), float(record[1])))
    start_range += 1


# Display words randomly one after the other.
def refresh_func():
    tree = ttk.Treeview(root)
    tree.pack(side='top', fill=tkinter.BOTH, expand=True)
    root.after(1000, refresh_func)


root.after(0, refresh_func)
root.mainloop()
