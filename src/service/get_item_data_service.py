from selenium.webdriver.common.by import By
from src.service.selenium_contextmanager import WebDriver

def get_item_data(state : dict):

    if(state["site"] == "go_go_sing"):
        title, price, img, reviews = get_item_data_from_go_go_sing(state["urls"])
    if(state["site"] == "ki_jac_nyeo"):
        title, price, img, reviews = get_item_data_from_ki_jac_nyeo(state["urls"])
    if(state["site"] == "ki_jac_nam"):
        title, price, img, reviews = get_item_data_from_ki_jac_nam(state["urls"])
    if(state["site"] == "so_nyeo_na_ra"):
        title, price, img, reviews = get_item_data_from_so_nyeo_na_ra(state["urls"])

    result = {
        "site" : state["site"],
        "category" : state["category"],
        "title" : title,
        "image_link" : img,
        "price" : price,
        "reviews" : reviews
    }

    return result
    

# Crawling items from go go sing
def get_item_data_from_go_go_sing(urls:list):

    with WebDriver() as driver:

        for url in urls:
            driver.implicitly_wait(5)

            driver.get(url)

            driver.implicitly_wait(5)

            title = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/h3").text
            price = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td/span/strong").text
            img = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/a/img").get_attribute("src")
            
            reviews_frame = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[8]/div[16]/iframe')

            driver.switch_to.frame(reviews_frame)

            find_reviews = driver.find_elements(By.XPATH, "/html/body/div/div/div/div/div/ul/li/div/div/div/div/div/div")
            
            reviews = []
            for find_review in find_reviews:
                reviews.append(find_review.text)
            
            reviews = " ".join(reviews)

            return title, price, img, reviews


# Crawling items from ki jac nyeo
def get_item_data_from_ki_jac_nyeo(urls:list):

    with WebDriver() as driver:

        for url in urls:
            driver.implicitly_wait(5)

            driver.get(url)

            driver.implicitly_wait(5)

            title = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/ul/li[1]/div[2]/div[1]/span").text
            price = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/ul/li[1]/div[5]/table/tbody/tr[2]/td/span/strong").text
            img = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[2]/div/img").get_attribute("src")
            
            find_reviews = driver.find_elements(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/table/tbody/tr/td/div/div")
            
            reviews = []
            for find_review in find_reviews:
                reviews.append(find_review.text.replace("\n",""))
            
            reviews = " ".join(reviews)

            return title, price, img, reviews


# Crawling items from ki jac nam
def get_item_data_from_ki_jac_nam(urls:list):

    with WebDriver() as driver:

        for url in urls:
            driver.implicitly_wait(5)

            driver.get(url)

            driver.implicitly_wait(5)

            title = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[4]/h1").text
            price = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/span").text
            img = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/div/img").get_attribute("src")
            
            reviews_frame = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/div[2]/div[4]/div[1]/iframe[2]')

            review_link = reviews_frame.get_attribute("src")

            driver.get(review_link)

            find_reviews = driver.find_elements(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/table/tbody/tr/td/div/div")
            
            reviews = []
            for find_review in find_reviews:
                reviews.append(find_review.text)
            
            reviews = " ".join(reviews)

            return title, price, img, reviews


# Crawling items from so nyeo na ra
def get_item_data_from_so_nyeo_na_ra(urls:list):

    with WebDriver() as driver:

        for url in urls:
            driver.implicitly_wait(5)

            driver.get(url)

            driver.implicitly_wait(5)

            title = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div[1]/div[2]/div[1]/div[1]").text
            price = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/span[3]/em").text
            img = driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div[1]/div[1]/div/div[1]/div/img").get_attribute("src")
            
            reviews_frame = driver.find_element(By.XPATH, '/html/body/div[4]/section/div[2]/div/iframe')

            driver.switch_to.frame(reviews_frame)

            find_reviews = driver.find_elements(By.XPATH, "/html/body/div/div/div/div/form/fieldset/ul/li/div/p")
            
            reviews = []
            for find_review in find_reviews:
                reviews.append(find_review.text)
            
            reviews = " ".join(reviews)

            return title, price, img, reviews