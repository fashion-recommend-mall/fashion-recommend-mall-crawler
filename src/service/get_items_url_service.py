from selenium.webdriver.common.by import By
from src.service.selenium_contextmanager import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def _valid_url(a_list : list[WebElement]):

    temp_list = []

    for a in a_list:

        url = a.get_attribute("href")

        if "javascript" in url :

            url = url.split("javascript")[0]

        if url != "":

            temp_list.append(a.get_attribute("href").split("javascript")[0])

    return temp_list


def get_items_url(state : dict):

    url_list = []

    with WebDriver() as driver:

        for page in range(1, int(state["pages"])+1):

            driver.implicitly_wait(5)

            driver.get(state["base_url"] + f"&page={page}")

            driver.implicitly_wait(5)

            a_list = driver.find_elements(By.XPATH, state["x_path"])

            driver.implicitly_wait(5)

            url_list.extend(_valid_url(a_list))

    return { "site" : state["key"] , "category" : state["category"], "urls" : url_list}