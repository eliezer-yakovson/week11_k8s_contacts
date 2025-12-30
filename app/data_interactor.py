import os
from pymongo import MongoClient
from bson import ObjectId

class DataInteractor:
    def __init__(self):
        self.mongo_host = os.getenv("MONGO_HOST", "localhost")
        self.mongo_port = os.getenv("MONGO_PORT", "27017")
        self.mongo_db = os.getenv("MONGO_DB", "contactsdb")

        self.client = MongoClient(f"mongodb://{self.mongo_host}:{self.mongo_port}/")
        self.db = self.client[self.mongo_db]
        self.contacts_collection = self.db["contacts"]

    def create_contact(self, contact_data):
        contact_id = self.contacts_collection.insert_one(contact_data).inserted_id
        return str(contact_id)

    def get_all_contacts(self):
        contacts = self.contacts_collection.find()

