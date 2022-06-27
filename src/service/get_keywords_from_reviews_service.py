"""
This is Get Keywords From Review Module
"""
import copy

import jpype
from konlpy.tag import Okt

from src.celery_setting import app
from project_setting import tool_setting


DatabaseDriver = tool_setting["database_driver"]


@app.task
def get_keywords_from_reviews(state : dict) -> dict:
    """
    Title : get_keywords_from_reviews

    It is working for getting Adjective and Noun from review!

    It uses konlpy module!

    So, Before use, install JVM over 11!

    Args :
        - state (dict) : this has data like below
        {
            site : str,
            category : str,
            title : str,
            image_link : str,
            price : st,
            reviews : str
        }

    Returns :
        - result (list) : this has list include below
        {
            site : str,
            category : str,
            title : str,
            image_link : str,
            price : st,
            reviews : list<str>
        }
    """

    okt = Okt()

    jpype.attachThreadToJVM()

    def reviews_filter(reviews):
        return reviews[1] == "Adjective" or reviews[1] == "Noun"

    reviews = state["reviews"]

    filterd_reivews = list(filter(reviews_filter, okt.pos(reviews)))

    review_result = []
    for review in filterd_reivews:
        review_result.append(review[0])

    result = {
        "site" : state["site"],
        "category" : state["category"],
        "title" : state["title"],
        "image_link" : state["image_link"],
        "price" : state["price"],
        "reviews" : review_result
    }

    with DatabaseDriver() as driver: # type: ignore
        driver.layer3.insert_one(copy.deepcopy(result))

    return result
