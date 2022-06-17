from selenium import webdriver
from service.get_items_url_service import GetItemUrlService
import json

with open('targets.json') as f:
	targets = json.load(f)

getItemUrlService = GetItemUrlService()

for target in targets["go_go_sing"]:
    result = getItemUrlService.get_items_url(target)
    print(result)
