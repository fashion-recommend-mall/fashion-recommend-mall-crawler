from abc import *

class Robot(metaclass=ABCMeta):

    @abstractmethod
    def get_item_url(self):
        pass
    
    @abstractmethod
    def get_item_data(self):
        pass
    
    @abstractmethod
    def get_keywords_from_reviews(self):
        pass

    @abstractmethod
    def get_style_from_img(self):
        pass