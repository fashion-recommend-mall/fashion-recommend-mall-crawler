from src.service.get_items_url_service import get_items_url
from src.service.get_item_data_service import get_item_data
from src.service.get_keywords_from_reviews_service import get_keywords_from_reviews
from src.service.get_style_from_img_service import get_sytle_from_img


class Robot():

    def __init__(self, states:dict):
        self.states = states
        self.item_url_list : list[str] = []


    def run(self):

        self.item_url_list = get_items_url(self.states)

        for url in self.item_url_list:
            result = get_item_data.s(url) | get_keywords_from_reviews.s() | get_sytle_from_img.s()
            result()

    def test(self):
        test = {'site': 'go_go_sing', 'category': 'Top', 'url': 'https://www.ggsing.com/product/%EC%BC%80%EC%9D%B4%EB%B8%94-%EB%B6%80%ED%81%B4-%EB%8B%88%ED%8A%B8%EC%A1%B0%EB%81%BC-%EB%B8%8C%EC%9D%B4%EB%84%A5%ED%81%AC%EB%A1%AD7%EA%B2%8C%EC%9D%B4%EC%A7%802%ED%95%A9%EA%B0%80%EB%91%98%EB%A0%88/58249/category/31/display/1/'}

        layer1 = get_item_data(test)
        print(layer1)
        layer2 = get_keywords_from_reviews(layer1)
        print(layer2)

        get_sytle_from_img(layer2)
        print("done")
