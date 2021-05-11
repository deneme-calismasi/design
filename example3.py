import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from pandas import DataFrame
from pyModbusTCP.client import ModbusClient
import pymongo
from itertools import count
import datetime
import datetime as dt
import threading
import time
import numpy as np
from itertools import chain


def executeSomething():
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

    time_data = datetime.datetime.now()
    print(time_data)

    def get_random_number():
        return random.uniform(1, 160)

    start = 1
    start_range = 50

    value = [[num for num in range(start, start + start_range)],
             [num for num in range(start, start + start_range)],
             data_as_float]

    data = np.array(value).T.tolist()
    # print(data)

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
    print(documents)

    # myclient.drop_database('Modbus_Database')
    mycol.delete_many({})
    time.sleep(5)


while True:
    executeSomething()
