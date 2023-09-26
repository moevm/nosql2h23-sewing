from pymongo import MongoClient

conn_string = "mongodb://localhost/"
client = MongoClient(conn_string)

database_name = "sewing"
users_collection = client[database_name]["users"]


def create_user(email, password_hash):
    users_collection = client[database_name]["users"]
    users_collection.insert_one({
        "user_id": users_collection.count_documents({}),
        "email": email,
        "password": password_hash,
    })


def get_users():
    for user in users_collection.find():
        print(user)


print(get_users())
print("---------------------")
create_user(
    email="Philipez@yandex.ru",
    password_hash="afsfasf"
)

print(get_users())
