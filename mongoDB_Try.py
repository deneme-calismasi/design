import numpy as np
import pymongo

start = 1
start_range = 4

array1 = [99, 98, 97, 96]
id_num = [num for num in range(start, start + start_range)]

print(array1)

print(id_num)

array_dictionary = dict(zip(id_num, array1))

print(array_dictionary)

"""
dict_created = array_dictionary

res_array = np.array(list(dict_created.items()))

# printing the converted array
print(res_array)
"""

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Modbus_Database"]

myclient.drop_database('Modbus_Database')

# mycol = mydb["collection1"]

# mydict = {"_id": 1, "name": "John", "address": "Highway 37"}

# print(mydict)

# x = mycol.insert_one(mydict)

print(myclient.list_database_names())

print(mydb.list_collection_names())

# print(x)

# data_find = mycol.find_one()

# print(data_find)

# res_array = np.array(list(data_find.items()))

# printing the converted array
# print(res_array)
