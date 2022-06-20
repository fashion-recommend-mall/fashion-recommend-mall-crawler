from selenium import webdriver
from src.service.get_items_url_service import get_items_url
from src.service.get_item_data_service import get_item_data
import json

with open('targets.json') as f:
	targets = json.load(f)

test_target = {
'site':'so_nyeo_na_ra',
'category': "top",
"urls" : [
'https://www.sonyunara.com/shop/view.php?index_no=215269',
]
}

print(get_item_data(test_target))