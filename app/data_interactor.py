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
        return [self.contact_to_dict(contact) for contact in contacts]

    def update_contact(self, id, contact_data):
        result = self.contacts_collection.update_one({"_id": ObjectId(id)}, {"$set": contact_data})
        return result.modified_count > 0

    def delete_contact(self, id):
        result = self.contacts_collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

    @staticmethod
    def contact_to_dict(contact):
        return {
            "id": str(contact["_id"]), 
            "first_name": contact["first_name"],
            "last_name": contact["last_name"],
            "phone_number": contact["phone_number"]
        }

    # def get_all_contacts(self):
    #     contacts = self.contacts_collection.find()
    #     return [{"id": str(contact["_id"]), "first_name": contact["first_name"], "last_name": contact["last_name"], "phone_number": contact["phone_number"]} for contact in contacts]
    
    def check_db(self):
        try:
            self.client.admin.command("ping")
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False
    

