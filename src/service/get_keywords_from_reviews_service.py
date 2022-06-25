import jpype
from konlpy.tag import Okt

from src.celery_setting import app
from src.tools.setting import tool_setting

DatabaseDriver = tool_setting["database_driver"]

@app.task
def get_keywords_from_reviews(state : dict) :

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

    with DatabaseDriver() as driver:
        driver.layer3.insert_one(result)

    return result
