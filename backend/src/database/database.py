import datetime

from pymongo import MongoClient

import bcrypt
from pydantic import EmailStr


class DatabaseService:
    def __init__(self, dsn: str):
        self.client = MongoClient(dsn)

        database_name = "sewing"
        self.customers_collection = self.client[database_name]["customers"]
        self.companies_collection = self.client[database_name]["companies"]
        self.messages_collection = self.client[database_name]["messages"]
        self.orders_collection = self.client[database_name]["orders"]
        self.models_collection = self.client[database_name]["models"]

    def get_model(self):
        return self.models_collection.find_one({}, {'_id': False})

    def load_model(self, model, path_to_model, model_type='', attaches_to=None, description=''):
        if attaches_to is None:
            attaches_to = []
        file_path = f"../models/{path_to_model}"
        with open(file_path, "wb") as f:
            f.write(model)
        self.models_collection.insert_one({
            "_id": self.models_collection.count_documents({}),
            "path_to_model": path_to_model,
            "type": model_type,
            "attaches_to": attaches_to,
            "description": description
        })

    async def register_company(self, email: EmailStr, password: str, TIN: str, name: str, contact_person: str, phone: str):
        hashed_password = bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt())
        self.companies_collection.insert_one({
            "_id": self.companies_collection.count_documents({}),
            "email": email,
            "hashed_password": hashed_password,
            "TIN": TIN,
            "name": name,
            "contact_person": contact_person,
            "phone": phone,
            "status": "Need to approve",
            "orders": [],
            "created_at": datetime.datetime.now(),
            "about": ""
        })

        return self.companies_collection.find_one({"email": email}, {"_id": False})

    async def get_company(self, email: EmailStr):
        return self.companies_collection.find_one({"email": email}, {"_id": False})

    async def register_customer(self, email: EmailStr, password: str, TIN: str, name: str, contact_person: str, phone: str):
        hashed_password = bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt())
        self.customers_collection.insert_one({
            "_id": self.customers_collection.count_documents({}),
            "email": email,
            "hashed_password": hashed_password,
            "TIN": TIN,
            "name": name,
            "contact_person": contact_person,
            "phone": phone,
            "status": "Need to approve",
            "orders": [],
            "created_at": datetime.datetime.now(),
            "about": ""
        })

        return self.customers_collection.find_one({"email": email}, {"_id": False})

    async def get_customer(self, email: EmailStr):
        return self.customers_collection.find_one({"email": email}, {"_id": False})