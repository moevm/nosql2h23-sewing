import datetime

from pymongo import MongoClient


conn_string = "mongodb://flints:moretechababa@154.194.53.172:27017"
client = MongoClient(conn_string)

database_name = "lensiz"
customers_collection = client[database_name]["customers"]
companies_collection = client[database_name]["companies"]
messages_collection = client[database_name]["messages"]
orders_collection = client[database_name]["orders"]
models_collection = client[database_name]["models"]


def get_model():
    return models_collection.find_one({}, {'_id': False})


def load_model(model, path_to_model, model_type='', attaches_to=[], description=''):
    file_path = f"../models/{path_to_model}"
    with open(file_path, "wb") as f:
        f.write(model)
    models_collection.insert_one({
        "_id": models_collection.count_documents(),
        "path_to_model": path_to_model,
        "type": model_type,
        "attaches_to": attaches_to,
        "description": description
    })


if __name__ == "__main__":
    pass
    # print(get_fullness_of_deps(datetime.datetime.now()))