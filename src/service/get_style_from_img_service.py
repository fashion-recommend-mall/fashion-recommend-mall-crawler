import requests

def get_sytle_from_img(state : dict) :

    for result in state["result"]:

        image_link = result["image_link"]

        style = requests.get(f'http://localhost:3000/upload?img_path={image_link}').json()
    
        result = {
            "site" : result["site"],
            "category" : result["category"],
            "title" : result["title"],
            "image_link" : result["image_link"],
            "price" : result["price"],
            "reviews" : result["reviews"],
            "style" : style
        }

        print(result)