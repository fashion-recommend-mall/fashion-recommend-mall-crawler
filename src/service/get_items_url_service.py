"""
This is Get Items URL Module
"""
import copy

from selenium.webdriver.common.by import By

from src.celery_setting import app
from project_setting import tool_setting


WebDriver  = tool_setting["web_driver"]
DatabaseDriver  = tool_setting["database_driver"]


def _valid_url(a_list : list) -> list:
    """
    Title : _valid_url

    It is working for valid href tag list to str list

    Some site witch made by php, tag has javascript code, so it also delete it

    Args :
        - a_list (list) : this is href tag list

    Returns :
        - result_list (list) : this is str list from href tag list
    """
    temp_list = []

    for find_a in a_list:

        url = find_a.get_attribute("href")

        if "javascript" in url :

            url = url.split("javascript")[0]

        if url != "":

            temp_list.append(find_a.get_attribute("href").split("javascript")[0])

    return temp_list


@app.task
def get_items_url(states : dict) -> list:
    """
    Title : get_items_url

    It is get item url from each site

    Args :
        - state (dict) : this has data like below
        {
            key : str
            category : str,
            base_url : str,
            x_path : str,
            pages" : int
        },

    Returns :
        - result (list) : this has list include below
        [
            {
                site : str,
                category : str,
                url : str
            },
            ...
        ]
    """

    result_list = []

    with WebDriver() as driver: # type: ignore

        for state in states["targets"]:

            for page in range(1, int(state["pages"])+1):

                driver.implicitly_wait(5)

                driver.get(state["base_url"] + f"&page={page}")

                driver.implicitly_wait(5)

                a_list = driver.find_elements(By.XPATH, state["x_path"])

                driver.implicitly_wait(5)

                for url in _valid_url(a_list):
                    result = { "site" : state["key"] , "category" : state["category"], "url" : url}
                    result_list.append(result)

    with DatabaseDriver() as driver: # type: ignore
        driver.layer1.insert_one(copy.deepcopy(result_list))

    return result_list
