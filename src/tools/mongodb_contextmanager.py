"""
This is Mongodb context manager!
"""
import certifi
from pymongo import MongoClient

from project_setting import url_setting

mongo_db_url : str = url_setting["mongo_db_url"]

class MongodbContextManager:
    """
    Title : MongodbContextManager

    This class is to deal mongodb with context manager!

    mongodb doesn't needs context manager

    Because Mongodb handle connector themselves

    Why makes this one?

    If you want to use another database?

    Make their context manager, and register them in project_setting.py!

    Attributes:
        - __enter__
        - __exit__
    """
    def __init__(self):
        self._ca = certifi.where()  # type: ignore
        self.client = MongoClient(mongo_db_url,tlsCAFile=self._ca)
        self._db = self.client.mall # type: ignore

    def __enter__(self):
        return self._db

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
