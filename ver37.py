import plotly.express as px
import pandas as pd
import pandas as df
import random
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from pyModbusTCP.client import ModbusClient
import pymongo
from itertools import count
import datetime
import datetime as dt
import time
from tkinter import Tk
import threading

sensor_no = ModbusClient(host="192.40.50.107", port=10010, unit_id=1, auto_open=True)
sensor_no.open()
regs = sensor_no.read_holding_registers(0, 100)
if regs:
    print(regs)
else:
    print("read error")

n = 0
data_count = 0

for n in range(50):
    data_count = n * 2
    regs[data_count], regs[data_count + 1] = regs[data_count + 1], regs[data_count]

dec_array = regs

data_bytes = np.array(dec_array, dtype=np.uint16)
data_as_float = data_bytes.view(dtype=np.float32)

time_data = dt.datetime.now().strftime('%Y-%m-%d %X')
print("time_data", time_data)

start = 1
start_range = 50

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

# myclient.drop_database('Modbus_Database')
# mycol.delete_many({})
# time.sleep(3)

# myquery = {"Sensor No": "2"}
myquery = {"Time": {"$gte": "2021-05-31 13:14:58", "$lt": time_data}}
mydoc = mycol.find(myquery)

for x in mydoc:
    print("mydoc:", x)

mydoc_all = mycol.find()
df = pd.DataFrame(list(mydoc_all))
df.to_csv("abc.csv", sep=",")

xs_doc = list(
    mycol.find(
        {"$and": [{"Sensor No": "12"}, {"Time": {"$gte": "2021-05-31 13:14:58", "$lt": time_data}}]},
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

nested_list = res
xs = [sub[2] for sub in xs_res]
ys = [sub[1] for sub in xs_res]

df = pd.read_csv('C:/Users/halilerhan.orun/IdeaProjects/calisma1/sensor_no.csv')

fig = px.line(df, x='Time', y='Temp', title='Date Series with Range Slider and Selectors')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

if __name__ == '__main__':
    fig.show()
