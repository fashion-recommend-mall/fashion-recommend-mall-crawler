from selenium import webdriver
from service.get_items_url_service import get_items_url_all
import json

with open('targets.json') as f:
	targets = json.load(f)

get_items_url_all(targets["targets"])