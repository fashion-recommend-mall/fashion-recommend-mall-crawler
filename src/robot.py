import time
from src.service.get_items_url_service import get_items_url
from src.service.get_item_data_service import get_item_data
from src.service.get_keywords_from_reviews_service import get_keywords_from_reviews
from src.service.get_style_from_img_service import get_sytle_from_img
from src.service.celery_setting import app
from celery import chain

def check_time(original_function):
    def inner_function(*args, **kwargs):
        start_time = time.perf_counter()
        result = original_function(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {original_function.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return inner_function

    
class Robot():

    def __init__(self, states:dict):
        self.states = states

    @check_time
    def run(self):
        for state in self.states["targets"]:
            self.make_index(state)

    def make_index(self, state:dict):

        layer1 = get_items_url(state)

        layer2 = get_item_data(layer1)

        layer3 = get_keywords_from_reviews(layer2)

        get_sytle_from_img(layer3)



