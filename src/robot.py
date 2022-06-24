from src.service.get_items_url_service import get_items_url
from src.service.get_item_data_service import get_item_data
from src.service.get_keywords_from_reviews_service import get_keywords_from_reviews
from src.service.get_style_from_img_service import get_sytle_from_img


class Robot():

    def __init__(self, states:dict):
        self.states = states
        self.item_url_list = []


    def run(self):

        self.item_url_list = get_items_url(self.states)

        for url in self.item_url_list:
            result = get_item_data.s(url) | get_keywords_from_reviews.s() | get_sytle_from_img.s()
            result()
