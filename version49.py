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

# import threading

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


# threading.Timer(2.0, fig.show).start()
# myclient.drop_database('Modbus_Database')
# mycol.delete_many({})
# time.sleep(3)

def on_double_click(event):
    item = tree.identify('item', event.x, event.y)
    print(tree.item(item, "text"))

    xs_doc = list(
        mycol.find(
            {"$and": [{"Sensor No": tree.item(item, "text")},
                      {"Time": {"$gte": "2021-05-31 13:14:58", "$lt": time_data}}]},
            {'_id': 0}))

    print(xs_doc)
    xs_res = [list(idx.values()) for idx in xs_doc]

    df = pd.DataFrame(list(xs_doc))
    df.to_csv("sensor_no.csv", sep=",")

    for index1, row in enumerate(xs_res):
        for index2, item in enumerate(row):
            try:
                xs_res[index1][index2] = (float(item))
            except ValueError:
                pass


# myquery = {"Sensor No": "2"}
myquery = {"Time": {"$gte": "2021-05-31 13:14:58", "$lt": time_data}}
mydoc = mycol.find(myquery)

mydoc_all = mycol.find()
df = pd.DataFrame(list(mydoc_all))
df.to_csv("abc.csv", sep=",")

df = pd.read_csv('C:/Users/halilerhan.orun/IdeaProjects/calisma1/sensor_no.csv')
fig = px.line(df, x='Time', y='Temp', title='Temperature °C - Time', color='Sensor No')
# fig.data[0].update(mode='markers+lines')

fig.update_xaxes(
    rangeslider_visible=True,
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

tree.bind("<Double-1>", on_double_click)

start_range = 0

for record in res[-(start_regs // 2):]:
    tree.insert("", index='end', text="%s" % int(record[0]), iid=start_range,
                values=(str(record[2]), int(record[0]), float(record[1])))
    start_range += 1


# tree = ttk.Style()
# tree.configure('Treeview', rowheight=30)


def _quit():
    root.quit()
    root.destroy()


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open Calendar')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=_quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Figure', command=fig.show)
helpmenu.add_command(label='About')

if __name__ == '__main__':
    root.mainloop()
