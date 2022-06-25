from pymongo import MongoClient
import certifi

class MongodbContextManager:
    def __init__(self):
        self.ca = certifi.where()
        self.client = MongoClient("mongodb+srv://admin:emm05235@cluster0.umzeh.mongodb.net/" \
                             "myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=self.ca)
        self.db = self.client.mall

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        return None