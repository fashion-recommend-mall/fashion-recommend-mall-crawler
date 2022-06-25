from src.tools.mongodb_contextmanager import MongodbContextManager
from src.tools.selenium_contextmanager import SeleniumContextManager


tool_setting = {
    "database_driver" : MongodbContextManager,
    "web_driver" : SeleniumContextManager
}
