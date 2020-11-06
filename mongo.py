import pymongo

class MongoClient():
    def __init__(self):
        super().__init__()
        self.client = pymongo.MongoClient("mongodb+srv://insta:Student1@cluster0.ioxxr.mongodb.net/instadb?retryWrites=true&w=majority")

    def db(self, name='instadb'):
        return self.client[name]
    
    def insert_one(self, data, coll):
        db = self.db()
        c = db[coll]
        c.insert_one(data)