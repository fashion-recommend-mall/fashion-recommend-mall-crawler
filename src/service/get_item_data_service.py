from selenium.webdriver.common.by import By
from src.service.selenium_contextmanager import WebDriver

def get_item_data(state : dict):

    if(state["site"] == "go_go_sing"):
        result= get_item_data_from_go_go_sing(state)
    if(state["site"] == "ki_jac_nyeo"):
        result = get_item_data_from_ki_jac_nyeo(state)
    if(state["site"] == "ki_jac_nam"):
        result = get_item_data_from_ki_jac_nam(state)
    if(state["site"] == "so_nyeo_na_ra"):
        result = get_item_data_from_so_nyeo_na_ra(state)

    return {"item_datas" : result}
    

# Crawling items from go go sing
def get_item_data_from_go_go_sing(state:dict):

    result_list =[]

    with WebDriver() as driver:

        for url in state["urls"]:

            driver.implicitly_wait(5)

            driver.get(url)

            driver.implicitly_wait(5)

            title = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/h3").text
            price = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td/span/strong").text
            img = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/a/img").get_attribute("src")
            
            reviews_frame = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[8]/div[16]/iframe')

            driver.switch_to.frame(reviews_frame)

            find_reviews = driver.find_elements(By.XPATH, "/html/body/div/div/div/div/div/ul/li/div/div/div/div/div/div")
            
            reviews_list = []
            for find_review in find_reviews:
                reviews_list.append(find_review.text)
            
            reviews = " ".join(reviews_list)

            result = {
                "site" : state["site"],
                "category" : state["category"],
                "title" : title,
                "image_link" : _img_url_to_http_from_https(img),
                "price" : price,
                "reviews" : reviews
            }

            result_list.append(result)
            
    return result_list


# Crawling items from ki jac nyeo
def get_item_data_from_ki_jac_nyeo(state:dict):

    result_list =[]

    with WebDriver() as driver:

        for url in state["urls"]:

            driver.implicitly_wait(5)

            driver.get(url)

            driver.implicitly_wait(5)

            title = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/ul/li[1]/div[2]/div[1]/span").text
            price = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/ul/li[1]/div[5]/table/tbody/tr[2]/td/span/strong").text
            img = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[2]/div/img").get_attribute("src")
            
            find_reviews = driver.find_elements(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/table/tbody/tr/td/div/div")
            
            reviews_list = []
            for find_review in find_reviews:
                reviews_list.append(find_review.text.replace("\n",""))


            reviews = " ".join(reviews_list) 

            result = {
                "site" : state["site"],
                "category" : state["category"],
                "title" : title,
                "image_link" : _img_url_to_http_from_https(img),
                "price" : price,
                "reviews" : reviews
            }

            result_list.append(result)
            
    return result_list


# Crawling items from ki jac nam
def get_item_data_from_ki_jac_nam(state:dict):

    result_list =[]

    with WebDriver() as driver:

        for url in state["urls"]:
            driver.implicitly_wait(5)

            driver.get(url)

            driver.implicitly_wait(5)

            title = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[3]/h1").text
            price = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[3]/div[5]/div/table/tbody[1]/tr[2]/td/strong/span").text
            img = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[2]/div[1]/p/a/img").get_attribute("src")
            
            reviews_frame = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/div[2]/div[4]/div[1]/iframe[2]')

            review_link = reviews_frame.get_attribute("src")

            driver.get(review_link)

            find_reviews = driver.find_elements(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/table/tbody/tr/td/div/div")
            
            reviews_list = []
            for find_review in find_reviews:
                reviews_list.append(find_review.text)
            
            reviews = " ".join(reviews_list)

            result = {
                "site" : state["site"],
                "category" : state["category"],
                "title" : title,
                "image_link" : _img_url_to_http_from_https(img),
                "price" : price,
                "reviews" : reviews
            }

            result_list.append(result)

    return result_list


# Crawling items from so nyeo na ra
def get_item_data_from_so_nyeo_na_ra(state:dict):

    result_list =[]

    with WebDriver() as driver:

        for url in state["urls"]:
            driver.implicitly_wait(5)

            driver.get(url)

            driver.implicitly_wait(5)

            title = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div[1]/div[2]/div[1]/div[1]").text
            price = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/span[3]/em").text
            img = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div[1]/div[1]/div/div[1]/div/img").get_attribute("src")
            
            reviews_frame = driver.find_element(By.XPATH, '/html/body/div[4]/section/div[2]/div/iframe')

            driver.switch_to.frame(reviews_frame)

            find_reviews = driver.find_elements(By.XPATH, "/html/body/div/div/div/div/form/fieldset/ul/li/div/p")
            
            reviews_list = []
            for find_review in find_reviews:
                reviews_list.append(find_review.text)
            
            reviews = " ".join(reviews_list)

            result = {
                "site" : state["site"],
                "category" : state["category"],
                "title" : title,
                "image_link" : _img_url_to_http_from_https(img),
                "price" : price,
                "reviews" : reviews
            }

            result_list.append(result)
            
    return result_list


def _img_url_to_http_from_https(url:str):
    return url.replace("https", "http")