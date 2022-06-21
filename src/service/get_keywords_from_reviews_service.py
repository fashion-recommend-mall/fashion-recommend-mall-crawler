from typing import Set
from konlpy.tag import Okt

okt = Okt()

def get_keywords_from_reviews(state : dict) :
    result_list = []
    for item_data in state["item_datas"]:
        result = reviews_filter(item_data)
        result_list.append(result)
    return {"result" : result_list}
        

def reviews_filter(state: dict):

    def check_type(reviews):
        return reviews[1] == "Adjective" or reviews[1] == "Noun"

    reviews = state["reviews"]

    filterd_reivews = list(filter(check_type, okt.pos(reviews)))

    review_result = []
    for review in filterd_reivews:
        review_result.append(review[0])
    
    result = {
        "site" : state["site"],
        "category" : state["category"],
        "title" : state["title"],
        "image_link" : state["image_link"],
        "price" : state["price"],
        "reviews" : list(set(review_result))
    }

    return result
