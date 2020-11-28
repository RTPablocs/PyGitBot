import pymongo
from repo import Repo


class MongoController:

    def __init__(self, db):
        self.db_uri = pymongo.MongoClient(db)
        self.db = self.db_uri["pygitbot"]
        self.collection = self.db["repos"]

    def create(self, repo):
        try:
            self.collection.insert_one(repo)
            print("Repo added")

        except pymongo.errors.DuplicateKeyError:
            print ("Skipping Addition, key exists")

    def read(self):
        repos = list(self.collection.find())
        print(repos, "\n Found {n} repos".format(n=len(repos)))

    def delete(self, id):
        self.collection.delete_one({"_id": id})
        print("Repo deleted from DB")

    def update(self, id, update_field, update_value):
        repo_id = {"_id": id}
        update = {"$set": {update_field: update_value}}
        self.collection.update_one(repo_id, update)



