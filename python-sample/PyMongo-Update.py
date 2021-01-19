import pymongo
import cosmosmongo

myclient = pymongo.MongoClient(cosmosmongo.mongoUrl)
mydb = myclient["hrdb"]
mycol = mydb["books"]

# 
def ShowAll():
    for b in mycol.find():
        print(b)

ShowAll()

#update one

mycol.update_one({"bookid":"100"}, {"$set":{"author":"James Joyce"}})

print("Record updated..")
ShowAll()