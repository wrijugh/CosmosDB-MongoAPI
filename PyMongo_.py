import pymongo 
import random

myclient = pymongo.MongoClient("mongodb://cosmosfreewg:6gUvMGLaGRvkgysbC6XnFZlBbvnqQxguWBlTDtZZcXtlkawL96Q0njCNGzDcwU1wW9L1QAdwszKzUVLxc9AT5g==@cosmosfreewg.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosfreewg@")

mydb = myclient["hrdb"]
mycol = mydb["employee"]

# print(mydb.list_collection_names())

i = random.randint(1, 1000)
newEmp1 = {"employeeId": str(i), "name": "Wrishika Ghosh", "job":"CEO"}

i = random.randint(1, 1000)
newEmp2 = {"employeeId": str(i), "name": "Saswati Sanyal", "job":"CFO"}

x = mycol.insert_one(newEmp1)
x = mycol.insert_one(newEmp2)

for emp in mycol.find():
    print(emp)