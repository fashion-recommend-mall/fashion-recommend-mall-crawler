"""
This module has robot class handling logics!
"""
from src.service.get_items_url_service import get_items_url
from src.service.get_item_data_service import get_item_data
from src.service.get_keywords_from_reviews_service import get_keywords_from_reviews
from src.service.get_style_from_img_service import get_sytle_from_img


class Robot():
    """
    This is Robot Class

    This class is used to recognize to barcode

    Attributes:
        run : This Function is running crawling logics!
    """
    def __init__(self, states:dict) -> None:
        """
        This is Robot Constructure!

        Args :
            - states (dict) : Should has targets from target.json!
        """
        self.states = states
        self.item_url_list : list[str] = []


    def run(self) -> None:
        """
        This is run method

        It will start crawling from 4 website

        Args :
            -

        Returns :
            -
        """
        self.item_url_list = get_items_url(self.states)

        for url in self.item_url_list:
            result = get_item_data.s(url) | get_keywords_from_reviews.s() | get_sytle_from_img.s()
            result()
