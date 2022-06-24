from selenium.webdriver.common.by import By
from src.tools.selenium_contextmanager import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from src.celery_setting import app


def _valid_url(a_list : list[WebElement]):

    temp_list = []

    for a in a_list:

        url = a.get_attribute("href")

        if "javascript" in url :

            url = url.split("javascript")[0]

        if url != "":

            temp_list.append(a.get_attribute("href").split("javascript")[0])

    return temp_list


@app.task
def get_items_url(states : dict):

    result_list = []

    with WebDriver() as driver:

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

    return result_list