import requests

from src.celery_setting import app

@app.task
def get_sytle_from_img(state : dict) :

    image_link = state["image_link"]

    style = requests.get(f'http://localhost:3000/upload?img_path={image_link}').json()

    result = {
        "site" : state["site"],
        "category" : state["category"],
        "title" : state["title"],
        "image_link" : state["image_link"],
        "price" : state["price"],
        "reviews" : state["reviews"],
        "style" : style
    }

    print(result)