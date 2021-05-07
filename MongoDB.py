import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Modbus_Database"]

mycol = mydb["collection1"]

# mydict = {"name": "John", "address": "Highway 37"}

# x = mycol.insert_one(mydict)

# y = mycol.find_one()

print(myclient.list_database_names())

print(mydb.list_collection_names())

dblist = myclient.list_database_names()
if "Modbus_Database" in dblist:
    print("The database exists.")
else:
    print("No Name")

# print(x.inserted_id)

# print(y)

mycol.drop()