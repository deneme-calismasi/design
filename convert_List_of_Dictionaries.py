import numpy as np

food = [{'pizza': 324, 'sandwich': 78, 'hot dog': 90}, {'hamburger': 124, 'cheeseburger': 44, 'jelly belly': 99}]

# printing original list
print("The original list is : " + str(food))

# Convert List of Dictionaries to List of Lists
# Using list comprehension
res = [[key for key in food[0].keys()], *[list(idx.values()) for idx in food]]

# printing result
print("The converted list : " + str(res))

list2 = [{'pizza': 324, 'sandwich': 78, 'hot dog': 90}, {'hamburger': 124, 'cheeseburger': 44, 'jelly belly': 99}]

# printing original list
print("The original list is : " + str(list2))

# Convert List of Dictionaries to List of Lists
# Using loop + enumerate()
res = []
for idx, sub in enumerate(list2, start=0):
    if idx == 0:
        res.append(list(sub.keys()))
        res.append(list(sub.values()))
    else:
        res.append(list(sub.values()))

# printing result
print("The converted list : " + str(res))
