import numpy as np
import pymongo
import matplotlib.pylab as plt

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Modbus_Database"]
mycol = mydb["collection1"]

start = 0
start_range = 15

array1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 80, 70, 60, 50, 40]
id_num = [num for num in range(start, start + start_range)]

array_dictionary = dict(zip(id_num, array1))

print(array_dictionary)

mycol.insert(array_dictionary)

b = mycol.find_one()

lists = sorted(b.items())  # sorted by key, return a list of tuples

x, y = zip(*lists)  # unpack a list of pairs into two tuples

plt.plot(x, y)
plt.show()

"""
dict_created = array_dictionary

res_array = np.array(list(dict_created.items()))

# printing the converted array
print(res_array)
"""
