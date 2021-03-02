import pymongo 
import random
import cosmosmongo

# myclient = pymongo.MongoClient(cosmosmongo.mongoUrl)
myclient = pymongo.MongoClient(cosmosmongo.mongoAtlasUrl)

mydb = myclient["hrdb"]
mycol = mydb["employee"]

# print(mydb.list_collection_names())

def insertRecord(_mycol):
    #Insert
    #i = random.randint(1, 1000)
    newEmp = {"employeeId": "0", "name": "Wrishika Ghosh", "job":"CEO"}
    mycol.insert_one(newEmp) #insert single document

    newEmps = [
        {"employeeId": "1", "name": "Picasso", "job" : "Cubist"},
        {"employeeId": "2", "name": "Claude Monet", "job" : "Impressionist"},
        {"employeeId": "3", "name": "Jackson Pollock", "job" : "Abstract Expressionist"},
        {"employeeId": "4", "name": "Cezan", "job" : "Post-Impressionist"}
    ]

    # Insert an array of documents - many
    mycol.insert_many(newEmps)

insertRecord(mycol)

def insertChildrenArray():
    employeeWithChildren = {
        "employeeId": "1",
        "name": "Wriju Ghosh",    
        "children":[
            {"name": "Sam", "dateOfBirth":"1997-08-01", "dep":False},
            {"name": "John", "dateOfBirth":"2007-08-01", "dep":False},
            {"name": "Mathew", "dateOfBirth":"1999-08-01", "dep":True}
        ]}
    mycol.insert_one(employeeWithChildren)

#insertChildrenArray()

#count 
count = mycol.count_documents({})
print(count)#
#delete record 
def deleteAllRecords():
    mycol.delete_many({})
# deleteAllRecords()

#Show all documents one by one
for emp in mycol.find():    
    print(emp)

# Filter 
# def findSome():
#     mycol.aggregate([
#         {
#             $addFields: {
#                 numChildren:{$size:"$children"}
#             }
#         }
#     ])

