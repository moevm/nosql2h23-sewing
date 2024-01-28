import datetime

from pymongo import MongoClient

import bcrypt
from pydantic import EmailStr


class DatabaseService:
    def __init__(self, dsn: str):
        self.client = MongoClient(dsn)

        database_name = "lensiz"
        self.customers_collection = self.client[database_name]["customers"]
        self.companies_collection = self.client[database_name]["companies"]
        self.messages_collection = self.client[database_name]["messages"]
        self.orders_collection = self.client[database_name]["orders"]
        self.models_collection = self.client[database_name]["models"]
        self.translates_collection = self.client[database_name]["translates"]
        self.managers_collection = self.client[database_name]["managers"]
        self.settings_collection = self.client[database_name]["settings"]

    def get_model(self):
        return self.models_collection.find_one({}, {'_id': False})

    def get_manager(self, email):
        return self.managers_collection.find_one({"email": email}, {'_id': False})

    async def get_settings(self):
        return self.settings_collection.find_one({}, {"_id": False})

    async def update_settings(self, link_to_video, width_of_video, height_of_video):
        self.settings_collection.update_one({"_id": 0}, {"$set": {
            "link_to_video": link_to_video,
            "width_of_video": width_of_video,
            "height_of_video": height_of_video,
        }
        }, upsert=False)

    def load_model(self, name, model, path_to_model, model_type='', description=''):
        new_model_id = self.models_collection.find_one({"$query": {}, "$orderby": {"_id": -1}})["_id"] + 1

        self.models_collection.insert_one({
            "_id": new_model_id,
            "name": name,
            "model": model,
            "path_to_model": path_to_model,
            "type": model_type,
            "status": 0,
            "color_count": 1,
            "conflicts_to": [],
            "description": description
        })

    def update_model_text_fields(self, model_id, name, conflicts_to, status, color_count, model_type='',
                                 description=''):
        self.models_collection.update_one({"_id": model_id}, {"$set": {
            "name": name,
            "type": model_type,
            "conflicts_to": conflicts_to,
            "status": status,
            "description": description,
            "color_count": color_count
        }
        }, upsert=False)

    async def get_models_by_settings(self, work, sex, season):
        start_string = f"{work}/{season}/{sex}"
        return self.models_collection.find({"path_to_model": {"$regex": f"^{start_string}"}, "status": 0})

    async def get_all_models(self):
        return self.models_collection.find({})

    async def get_model_by_id(self, model_id):
        return self.models_collection.find_one({"_id": int(model_id)})

    async def get_company(self, user_id):
        return self.companies_collection.find_one({"_id": int(user_id)})

    async def get_customer(self, user_id):
        return self.customers_collection.find_one({"_id": int(user_id)})

    def update_user_text_fields(self, user_id, email, role, TIN, name, contact_person, phone,
                                status, about):
        collection = self.customers_collection
        if role == "company":
            collection = self.companies_collection

        collection.update_one({"_id": user_id}, {"$set": {
            "email": email,
            "TIN": TIN,
            "name": name,
            "contact_person": contact_person,
            "phone": phone,
            "status": status,
            "about": about
        }
        }, upsert=False)

    async def get_translates(self):
        return self.translates_collection.find_one({})

    async def create_manager(self, name: str, email: str, password: str, about: str):
        hashed_password = bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt())
        self.managers_collection.insert_one({
            "name": name,
            "email": email,
            "hashed_password": hashed_password,
            "about": about,
        })

    async def save_layout(self, email, elements, name, elements_color, active_elements, elements_to_models, last_element_id):
        self.customers_collection.update_one({"email": email}, {"$push": {
            "orders": {
                "elements": elements,
                "manager": None,
                "name": name,
                "elements_color": elements_color,
                "active_elements": active_elements,
                "elements_to_models": elements_to_models,
                "last_element_id": last_element_id,
            }
        }})

    async def register_company(self,
                               email: EmailStr, password: str, TIN: str, name: str, contact_person: str, phone: str):
        hashed_password = bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt())
        self.companies_collection.insert_one({
            "_id": self.companies_collection.count_documents({}),
            "email": email,
            "role": "company",
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

    async def register_customer(self, email: EmailStr, password: str, TIN: str, name: str, contact_person: str,
                                phone: str):
        hashed_password = bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt())
        self.customers_collection.insert_one({
            "_id": self.customers_collection.count_documents({}),
            "email": email,
            "role": "customer",
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

    async def get_user(self, email: EmailStr):
        customer = self.customers_collection.find_one({"email": email}, {"_id": False})
        if not customer:
            return self.companies_collection.find_one({"email": email}, {"_id": False})
        return customer

    async def get_registration_applications(self):
        return {
            "customers": list(self.customers_collection.find({"status": "Need to approve"})),
            "companies": list(self.companies_collection.find({"status": "Need to approve"}))
        }

    async def customers(self, page, limit, find_options):
        return self.customers_collection.find(find_options).skip((page - 1) * limit).limit(limit)

    async def customers_count(self, options):
        return self.customers_collection.count_documents(options)

    async def companies(self, page, limit, find_options):
        return self.companies_collection.find(find_options).skip((page - 1) * limit).limit(limit)

    async def companies_count(self, options):
        return self.companies_collection.count_documents(options)

    async def approve_customer(self, id):
        return self.customers_collection.update_one({"_id": id}, {"$set": {"status": "Approved"}})

    async def decline_customer(self, id):
        return self.customers_collection.update_one({"_id": id}, {"$set": {"status": "Declined"}})

    async def approve_company(self, id):
        return self.companies_collection.update_one({"_id": id}, {"$set": {"status": "Approved"}})

    async def decline_company(self, id):
        return self.companies_collection.update_one({"_id": id}, {"$set": {"status": "Declined"}})
