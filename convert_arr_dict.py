products = [[1, 1, 99, 101]]
arr = []
for product in products:
    vals = {}
    vals["ID"] = int(product[0])
    vals["Sensor No"] = str(product[1])
    vals["IP"] = str(product[2])
    vals["Time"] = str(product[3])
    arr.append(vals)
print(arr)
