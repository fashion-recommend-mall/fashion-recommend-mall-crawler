from selenium import webdriver
from selenium.webdriver.common.by import By
from service.selenium_contextmanager import WebDriver
import celery
from celery import Task

app = celery.Celery(
    'get_item_urls',
    broker="pyamqp://guest@localhost",
    backend="rpc://guest@localhost"
)


def _init_driver():

    options = webdriver.ChromeOptions()

    options.add_argument('headless')

    options.add_argument('window-size=1920x1080')

    options.add_argument("disable-gpu")

    driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=options)

    return driver


def _valid_url(a_list : list[str]):

    temp_list = []

    for a in a_list:

        url = a.get_attribute("href")

        if "javascript" in url :

            url = url.split("javascript")[0]

        if url != "":

            temp_list.append(a.get_attribute("href").split("javascript")[0])

    return temp_list


@app.task
def get_items_url(state : dict):

    url_list = []

    with WebDriver(_init_driver()) as driver:

        for page in range(1, int(state["pages"])+1):

            driver.implicitly_wait(5)

            driver.get(state["base_url"] + f"&page={page}")

            driver.implicitly_wait(5)

            a_list = driver.find_elements(By.XPATH, state["x_path"])

            driver.implicitly_wait(5)

            url_list.extend(_valid_url(a_list))

    return { state["category"] : url_list }


@app.task
def get_items_url_all(targets : dict):

    g = celery.group(
        get_items_url.s(target) for target in targets
    )

    return g()