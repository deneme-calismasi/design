products = [[1, 1, 99], [2, 2, 98]]
arr = []
for product in products:
    vals = {}
    vals["ID"] = str(product[0])
    vals["Sensor No"] = str(product[1])
    vals["Temp"] = str(product[2])
    arr.append(vals)
print(arr)
