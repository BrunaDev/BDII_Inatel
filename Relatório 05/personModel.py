from pymongo import MongoClient
from bson.objectid import ObjectId

class PersonModel:
    def __init__(self, database):
        self.db = database

    def create_person(self, name:str, age: int):
        try:
            res = self.db.collection.insert_one({"name": name, "age": age})
            print(f"Person created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating person: {e}")
            return None

    def read_person_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Person found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading person: {e}")
            return None

    def update_person(self, id: str, name: str, age: int):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"name": name, "age": age}})
            print(f"Person updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating person: {e}")
            return None

    def delete_person(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Person deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting person: {e}")
            return None