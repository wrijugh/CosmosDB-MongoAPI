import pymongo 
import random
import cosmosmongo

myclient = pymongo.MongoClient(cosmosmongo.mongoAtlasUrl)

mydb = myclient["hrdb"]
mycol = mydb["feedback"]

def insertFeedback():

    newFeedbacks = [
        {"feedbackId":"1","comments":"MondoDG Atlas is costly"},
        {"feedbackId":"2","comments":"CosmosDB for MongoDB API is managed"},
        {"feedbackId":"3","comments":"MongoDB in CosmosDB don't support transaction"},
        {"feedbackId":"4","comments":"MongoDB supports document size 16 MB"},
        {"feedbackId":"5","comments":"MongoDB has seacrch"},
        {"feedbackId":"6","comments":"Pymongo Library was the choice"},
        {"feedbackId":"7","comments":"Python can connect both MongoDB and CosmosDB"}
    ]

    mycol.insert_many(newFeedbacks)
    print("===================Inserted=====================")

insertFeedback()

