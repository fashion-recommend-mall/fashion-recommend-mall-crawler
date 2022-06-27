"""
This is Get Item Data Module
"""
import copy

from selenium.webdriver.common.by import By

from src.celery_setting import app
from project_setting import tool_setting


WebDriver  = tool_setting["web_driver"]
DatabaseDriver  = tool_setting["database_driver"]


@app.task
def get_item_data(state : dict) -> dict:
    """
    Title : get_item_data

    It will crawling each item data

    Args :
        - state (dict) : this has data like below
        {
            site : str,
            category : str,
            url : str,
        }

    Returns :
        - result (ditc) : this has data like below
        {
            site : str,
            category : str,
            title : str,
            image_link : str,
            price : st,
            reviews : str
        }
    """
    if(state["site"] == "go_go_sing"):
        title, price, img, reviews = get_item_data_from_go_go_sing(state)

    elif(state["site"] == "ki_jac_nyeo"):
        title, price, img, reviews = get_item_data_from_ki_jac_nyeo(state)

    elif(state["site"] == "ki_jac_nam"):
        title, price, img, reviews = get_item_data_from_ki_jac_nam(state)

    else:
        title, price, img, reviews = get_item_data_from_so_nyeo_na_ra(state)

    result = {
        "site" : state["site"],
        "category" : state["category"],
        "title" : title,
        "image_link" : _img_url_to_http_from_https(img),
        "price" : price,
        "reviews" : reviews
    }

    with DatabaseDriver() as driver: # type: ignore
        driver.layer2.insert_one(copy.deepcopy(result))

    return result


# Crawling items from go go sing
def get_item_data_from_go_go_sing(state:dict) -> tuple:
    """
    Title : get_item_data_from_go_go_sing

    It is crawling item data from go go sing site

    Args :
        - state (dict) : this has data like below
        {
            site : str,
            category : str,
            url : str,
        }

    Returns :
        - result (ditc) : this has data like below
        {
            title : str,
            img : str,
            price : st,
            reviews : str
        }
    """

    with WebDriver() as driver: # type: ignore

        driver.implicitly_wait(5)
        driver.get(state["url"])

        driver.implicitly_wait(5)
        title = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/h3").text
        price = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]" \
            "/table/tbody/tr[2]/td/span/strong").text
        img = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]" \
                "/div[1]/a/img").get_attribute("src")

        reviews_frame = driver.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[8]/div[16]/iframe')
        driver.switch_to.frame(reviews_frame)
        find_reviews = driver.find_elements(
            By.XPATH, "/html/body/div/div/div/div/div/ul/li/div/div/div/div/div/div")

        reviews_list = []
        for find_review in find_reviews:
            reviews_list.append(find_review.text)

        reviews = " ".join(reviews_list)
        return title, price, img, reviews


# Crawling items from ki jac nyeo
def get_item_data_from_ki_jac_nyeo(state:dict) -> tuple:
    """
    Title : get_item_data_from_ki_jac_nyeo

    It is crawling item data from ki jac nyeo

    Args :
        - state (dict) : this has data like below
        {
            site : str,
            category : str,
            url : str,
        }

    Returns :
        - result (ditc) : this has data like below
        {
            title : str,
            img : str,
            price : st,
            reviews : str
        }
    """

    with WebDriver() as driver: # type: ignore

        driver.implicitly_wait(5)
        driver.get(state["url"])

        driver.implicitly_wait(5)
        title = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[4]/div[2]/div[1]/div/div[2]/div[1]"\
                "/div/ul/li[1]/div[2]/div[1]/span").text
        price = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[4]/div[2]/div[1]/div/div[2]/div[1]"\
                "/div/ul/li[1]/div[5]/table/tbody/tr[2]/td/span/strong").text
        img = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[2]"\
                "/div/img").get_attribute("src")

        find_reviews = driver.find_elements(
            By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/table/tbody/tr/td/div/div")

        reviews_list = []
        for find_review in find_reviews:
            reviews_list.append(find_review.text.replace("\n",""))
        reviews = " ".join(reviews_list)

        return title, price, img, reviews


# Crawling items from ki jac nam
def get_item_data_from_ki_jac_nam(state:dict) -> tuple:
    """
    Title : get_item_data_from_ki_jac_nam

    It is crawling item data from ki jac nam

    Args :
        - state (dict) : this has data like below
        {
            site : str,
            category : str,
            url : str,
        }

    Returns :
        - result (ditc) : this has data like below
        {
            title : str,
            img : str,
            price : st,
            reviews : str
        }
    """

    with WebDriver() as driver: # type: ignore

        driver.implicitly_wait(5)
        driver.get(state["url"])
        driver.implicitly_wait(5)
        title = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[3]/h1").text
        price = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[3]/div[5]/div/table"\
                "/tbody[1]/tr[2]/td/strong/span").text
        img = driver.find_element(
            By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/div[1]/p/a/img").get_attribute("src")

        reviews_frame = driver.find_element(
            By.XPATH, '/html/body/div[3]/div/div[4]/div[2]/div[4]/div[1]/iframe[2]')

        review_link = reviews_frame.get_attribute("src")

        driver.get(review_link)

        find_reviews = driver.find_elements(
            By.XPATH, "/html/body/div/div/div/div/div/div/div/div/table/tbody/tr/td/div/div")

        reviews_list = []
        for find_review in find_reviews:
            reviews_list.append(find_review.text)

        reviews = " ".join(reviews_list)
        return title, price, img, reviews


# Crawling items from so nyeo na ra
def get_item_data_from_so_nyeo_na_ra(state:dict) -> tuple:
    """
    Title : get_item_data_from_so_nyeo_na_ra

    It is crawling item data from so nyeo na ra

    Args :
        - state (dict) : this has data like below
        {
            site : str,
            category : str,
            url : str,
        }

    Returns :
        - result (ditc) : this has data like below
        {
            title : str,
            img : str,
            price : st,
            reviews : str
        }
    """

    with WebDriver() as driver: # type: ignore

        driver.implicitly_wait(5)
        driver.get(state["url"])

        driver.implicitly_wait(5)
        title = driver.find_element(
            By.XPATH, "/html/body/div[4]/section/div[2]/div/div[1]/div[2]/div[1]/div[1]").text
        price = driver.find_element(
            By.XPATH, "/html/body/div[4]/section/div[2]/div/div[1]" \
            "/div[2]/div[2]/div/div/div[3]/div[1]/span[3]/em").text
        img = driver.find_element(
            By.XPATH, "/html/body/div[4]/section/div[2]/div/div[1]" \
            "/div[1]/div/div[1]/div/img").get_attribute("src")

        reviews_frame = driver.find_element(
            By.XPATH, '/html/body/div[4]/section/div[2]/div/iframe')
        driver.switch_to.frame(reviews_frame)
        find_reviews = driver.find_elements(
            By.XPATH, "/html/body/div/div/div/div/form/fieldset/ul/li/div/p")

        reviews_list = []
        for find_review in find_reviews:
            reviews_list.append(find_review.text)

        reviews = " ".join(reviews_list)
        return title, price, img, reviews


def _img_url_to_http_from_https(url:str) -> str:
    """
    Title : _img_url_to_http_from_https

    If get image using https, Some times has error like Unceltified

    So, it converts https into http

    Args :
        - url (str) : img url

    Returns :
        - url (ditc) : replaced url
    """
    return url.replace("https", "http")
