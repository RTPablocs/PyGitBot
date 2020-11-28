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
    def create_all(self, repo_list):
        try: 
            self.collection.insert_many(repo_list)
            print("Repos Added")
        except pymongo.errors.BulkWriteError:
            print("Addition Failed, One or more keys exists, try updating")

    def read(self):
        repos = list(self.collection.find())
        print(repos, "\n Found {n} repos".format(n=len(repos)))
        return repos
    
    def read_one(self, id):
        repo_id = {"_id": id}
        repo = self.collection.find_one(repo_id)
        print (repo)
        

    def delete(self, id):
        self.collection.delete_one({"_id": id})
        print("Repo deleted from DB")

    def update(self, id, update_field, update_value):
        repo_id = {"_id": id}
        update = {"$set": {update_field: update_value}}
        self.collection.update_one(repo_id, update)



