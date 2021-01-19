import pymongo
import cosmosmongo

myclient = pymongo.MongoClient(cosmosmongo.mongoUrl)

mydb = myclient["hrdb"]
mycol = mydb["books"]

newBook = {"bookid": "103", "title": "Calculas 3", "author": "Apostol"}

newId = mycol.insert_one(newBook).inserted_id
newRecord = mycol.find_one({"_id": newId})
print(newRecord)r