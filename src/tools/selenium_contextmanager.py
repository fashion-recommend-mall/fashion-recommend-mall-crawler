import time
from selenium import webdriver

class SeleniumContextManager:
    def __init__(self):

        options = webdriver.ChromeOptions()

        options.add_argument('headless')

        options.add_argument('window-size=1920x1080')

        options.add_argument("disable-gpu")

        driver = webdriver.Chrome(executable_path='./src/tools/chromedriver.exe', chrome_options=options)

        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
        time.sleep(2)
    