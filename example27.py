import numpy as np
import pymongo
import matplotlib.pylab as plt

start = 1
start_range = 16

array1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 80, 70, 60, 50, 40, 30]
id_num = [num for num in range(start, start + start_range)]

array_dictionary = dict(zip(id_num, array1))

print(array_dictionary)

dictOfWords = {i: array1[i] for i in range(0, len(array1))}

print(dictOfWords)

i = 0
new_list = []
while i < len(array1):
    new_list.append(array1[i:i + 2])
    i += 2
print(new_list)

new_list2 = [array1[i:i + 2] for i in range(0, len(array1), 2)]
print(new_list2)


array_dictionary = dict(zip(id_num, new_list))

print(array_dictionary)

"""

data_list = [0,1,2,3,4,5,6,7,8]
    
new_list = gen_list_of_lists(original_list=data_list, new_structure=[3,3,3])
# The original desired outcome of [[0,1,2], [3,4,5], [6,7,8]]

new_list = gen_list_of_lists(original_list=data_list, new_structure=[2,3,3,1])
# [[0, 1], [2, 3, 4], [5, 6, 7], [8]]

"""