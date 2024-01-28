from pymongo import MongoClient

client = MongoClient("mongodb://lensiz:KVvI6xGIVoL6v4xb@82.202.173.204:27017/?retryWrites=true&w=majority")

database_name = "lensiz"
customers_collection = client[database_name]["customers"]
companies_collection = client[database_name]["companies"]
messages_collection = client[database_name]["messages"]
orders_collection = client[database_name]["orders"]
models_collection = client[database_name]["models"]
translates_collection = client[database_name]["translates"]

for i in range(27):
    models_collection.update_one({"_id": i}, {"$set": {
        "color_count": 1
    }
    }, upsert=False)
