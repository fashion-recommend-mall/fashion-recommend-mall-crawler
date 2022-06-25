import time
from selenium import webdriver

class SeleniumContextManager:
    def __init__(self):

        options = webdriver.ChromeOptions()

        options.add_argument('headless')

        options.add_argument('window-size=1920x1080')

        options.add_argument("disable-gpu")

        options.add_argument('--no-sandbox')

        options.add_argument("--single-process")
        
        options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome("/usr/src/chrome/chromedriver", chrome_options=options)

        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
        time.sleep(2)
    