import pymongo
import pandas as pd
import json
with open('config.json', 'r') as f:
    config = json.load(f)
username = config['username']
password = config['password']
cluster = config['cluster']

# Create connection to MongoDB Atlas
client = pymongo.MongoClient("mongodb+srv://" + username + ":" + password + " @" + cluster + "/?retryWrites=true&w=majority")
# Access database
db = client.stock
# Access collection
collection = db.stock_price
# Achieve the data stored inside of the collection
data = pd.DataFrame(list(collection.find()))
