from konlpy.tag import Okt

okt = Okt()

def get_keywords_from_reviews(state : dict) :

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

    return result