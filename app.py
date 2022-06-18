from selenium import webdriver
from service.get_items_url_service import get_items_url
import json

with open('targets.json') as f:
	targets = json.load(f)

for target in targets["go_go_sing"]:
    result = get_items_url.delay(target)
    print(result)
