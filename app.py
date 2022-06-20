from selenium import webdriver
from src.service.get_items_url_service import get_items_url
from src.service.get_item_data_service import get_item_data
from src.service.get_keywords_from_reviews_service import get_keywords_from_reviews
import json

with open('targets.json') as f:
	targets = json.load(f)

test_target = {'site': 'so_nyeo_na_ra', 'category': 'top', 'title': 'sgd7777 아일렛 꽈배기 아메카지 니트 조끼', 'image_link': 'https://img.sonyunara.com/files/goods/215269/1649398575_3.jpg', 'price': '16,500', 'reviews': '꽈배기+아일렛+크롭의 조합이라니!! 완전 귀여움 최강ㅠㅠㅠ 니트 두께가 많이 두껍지 않아서 초여름까지도 입을 수 있을 것 같아용 크롭 기장이라 다리가 길어보여서 키작녀분들께 더욱 추천드립니당ㅎㅎ 색감이 넘 예쁜 니트베스트 ! 청이나 검은색 하의에 다 잘어울리고 색감이나 뒷모습이 포인트가 돼서 넘 예뻐요 ♥ 여기저기 레이어드해 입기 좋아서 코디하기도 쉬워요 :) 앞뒤 구분없이 포인트를 주어 입기 좋아요 끈 조절이 되어서 체형에 맞게 조절이 가능하구요 여름에 두꺼운 감은 있지만 얇은 반팔 티셔츠와 레이어드해서 입으니 이뻐요 너무 예쁘고... 한번도 도전해본 적 없는 색상이었는데 너무 잘 어울리는거 같고.... 입어도 별로 안 덥고.... 너무 만족'}

print(get_keywords_from_reviews(test_target))