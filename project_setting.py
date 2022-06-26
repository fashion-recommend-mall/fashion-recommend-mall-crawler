"""
This is Project Settings

Check below!

url_setting 
    - Setting database(mondgodb atlas) and selenium urls!

tool_setting
    - Setting context manager to DI

celery_broker_url
    - Setting celery broker url!!
"""

from src.tools.mongodb_contextmanager import MongodbContextManager
from src.tools.selenium_contextmanager import SeleniumContextManager


url_setting = {
    "mongo_db_url" : "mongodb+srv://admin:emm05235@cluster0.umzeh.mongodb.net/" \
                             "myFirstDatabase?retryWrites=true&w=majority",
    "selenium_url" : "/usr/local/bin/chromedriver",
    "deep_learning_server_url" : "http://3.34.98.41:3000"
}


tool_setting = {
    "database_driver" : MongodbContextManager,
    "web_driver" : SeleniumContextManager
}


celery_broker_url = {
    "celery_broker_url" : "pyamqp://guest@3.34.5.27"
}
