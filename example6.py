import random
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
import time

regs = [16358, 8974, 78965, 12365, 45698, 12314, 4655, 4687, 132154, 54461, 46578, 1354, 4567, 13135, 1687, 464, 137,
        468432, 6444, 4684, 16358, 8974, 78965, 12365, 45698, 12314, 4655, 4687, 132054, 54061, 46570, 1054, 4567,
        13035, 1687, 464, 137, 40432, 6044, 4684, 16358, 8074, 78965, 12305, 45098, 12314, 4655, 4687, 10154, 16358,
        8974, 78965, 12365, 45698, 12314, 4655, 4687, 132154, 54461, 46578, 1354, 4567, 13135, 1687, 464, 137,
        468432, 6444, 4684, 16358, 8974, 78965, 12365, 45698, 12314, 4655, 4687, 132054, 54061, 46570, 1054, 4567,
        13035, 1687, 464, 137, 40432, 6044, 4684, 16358, 8074, 78965, 12305, 45098, 12314, 4655, 4687, 10154, 16358,
        8974]

n = 0
data_count = 0

for n in range(50):
    data_count = n * 2
    regs[data_count], regs[data_count + 1] = regs[data_count + 1], regs[data_count]

dec_array = regs

data_bytes = np.array(dec_array, dtype=np.uint16)
data_as_float = data_bytes.view(dtype=np.float32)

time_data = datetime.datetime.now()
print(time_data)

start = 1
start_range = 50

value = [[num for num in range(start, start + start_range)],
         [num for num in range(start, start + start_range)],
         data_as_float]
print("value :", value)

data = np.array(value).T.tolist()
print("data :", data)

products = data
arr = []
for product in products:
    vals = {}
    vals["Sensor No"] = str(int(product[1]))
    vals["Temp"] = str(product[2])
    vals["Time"] = str(time_data)
    arr.append(vals)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Modbus_Database"]

mycol = mydb["collection1"]

record_data = arr
mycol.insert_many(record_data)

documents = list(mycol.find({}, {'_id': 0}))
print("documents :", documents)

dict = np.array(documents)
print("dict :", dict)

res = [*[list(idx.values()) for idx in documents]]
res2 = [*[list(idx.values()) for idx in dict]]

# printing result
print("The converted documents : " + str(res))
print("The converted dict : " + str(res2))
