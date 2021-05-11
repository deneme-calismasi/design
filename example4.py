import random
from pyModbusTCP.client import ModbusClient
import datetime
import time
import numpy as np
import pymongo
import matplotlib.pyplot as plt


def execute_func():
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
    global documents
    documents = list(mycol.find({}, {'_id': 0}))
    print(documents)

    # myclient.drop_database('Modbus_Database')
    mycol.delete_many({})
    time.sleep(60)


while True:
    execute_func()

"""
global documents
sensor_number = [x['Sensor No'] for x in documents]
temp_number = [x['Temp'] for x in documents]

fig = plt.figure()

ax = fig.add_subplot(111)
ax.scatter(sensor_number, temp_number)

ax.set_xlabel("Sensor No")
ax.set_ylabel("Temp")

plt.show()
"""
