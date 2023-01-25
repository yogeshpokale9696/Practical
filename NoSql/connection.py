from pymongo import MongoClient

client = MongoClient("mongodb+srv://yogesh9696:pOkale-9692@cluster0.vl3qc5q.mongodb.net/?retryWrites=true&w=majority")

database = client["sp"]
collection = database["student"]

collection.insert_many([{"FirstName":"AAA","LastName":"BBB","Age":30,"gender":"M"},
                        {"FirstName":"CCC","LastName":"DDD","Age":35,"gender":"M"}])

#collection.update_many({"Age":{"$gt":30}},{'$set':{"Age":40}})    
#collection.delete_many({"Age":{"$gt":30}})
rs=collection.find({"Age":{"$gt":30}})

for i in rs:
    print(i)