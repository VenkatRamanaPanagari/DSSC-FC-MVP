import pymongo
client = pymongo.MongoClient("mongodb+srv://wilproject:BteIJ08DLS4Xs0yB@cluster0.umrzxzq.mongodb.net/?retryWrites=true&w=majority")
db = client.stock
print(db.list_collection_names())

# mongoimport --uri mongodb+srv://wilproject:BteIJ08DLS4Xs0yB@cluster0.umrzxzq.mongodb.net --collection stock --type CSV --headerline --file data.csv
# mongoimport --uri mongodb+srv://wilproject:BteIJ08DLS4Xs0yB@cluster0.umrzxzq.mongodb.net --collection stock --type CSV --headerline --file data.csv