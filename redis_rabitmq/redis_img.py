import requests
import redis
import io
from PIL import Image

redis_client = redis.Redis(host="localhost", port=6379, db=4)


def fetch_and_cache_image(api_url, key, expiration=None):
    response = requests.get(api_url)

    if response.status_code == 200:
        response = response.json()
        # username key
        name = response["results"][0]["name"]
        username = name["title"] + " " + name["first"] + " " + name["last"]
        # print(username)

        # image
        img_url = response["results"][0]["picture"]["medium"]
        img = requests.get(img_url)

        img_binary = img.content

        redis_client.set(username, img_binary)
    else:
        print("Failed to fetch image")


def get_cached_image(key):
    img_binary = redis_client.get(key)

    if img_binary:
        img = Image.open(io.BytesIO(img_binary))
        return img
    else:
        print("Image not found in cache")
        return None


api_url = "https://randomuser.me/api/"
# fetch_and_cache_image(api_url,"not_used")

img = get_cached_image("Mrs Candice Ruiz")

# print(redis_client.)