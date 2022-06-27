"""
This is Get Style From Img Module
"""
import requests

from src.celery_setting import app
from project_setting import tool_setting
from project_setting import url_setting


DatabaseDriver = tool_setting["database_driver"]
deep_learning_server_url : str = url_setting["deep_learning_server_url"]


@app.task
def get_sytle_from_img(state : dict) -> None:
    """
    Title : get_sytle_from_img

    It is working for getting Style from deep learning server

    So, Before use, Run deep learning server and input their url in project_setting.py

    Args :
        - state (dict) : this has data like below
        {
            site : str,
            category : str,
            title : str,
            image_link : str,
            price : st,
            reviews : list<str>
        }

    Returns :
        - None
    """

    image_link = state["image_link"]

    style = requests.get(f'{deep_learning_server_url}/upload?img_path={image_link}').json()

    result = {
        "site" : state["site"],
        "category" : state["category"],
        "title" : state["title"],
        "image_link" : state["image_link"],
        "price" : state["price"],
        "reviews" : state["reviews"],
        "style" : style
    }

    with DatabaseDriver() as driver: # type: ignore
        driver.layer4.insert_one(result)
