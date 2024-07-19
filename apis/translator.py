
import requests

def translate_to_eng(data):
    url="https://libretranslate.com/translate"
    payload = {
        "q": data,
        "source": "auto",  # Auto-detect the source language
        "target": "en",    # Target language is English
        "format": "text"
    }
    headers={"Content-Type":"application/json"}

    try:
        response = requests.post(url,json=payload,headers=headers)
        response.raise_for_status() # raise HTTPEror for bad rresponse (4xx or 5xx)
        translated_data = response.json()["translatedText"]
        print(translated_data)
        # return translated_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occured: {http_err}")
    except Exception as err:
        print(f"Error : {err}")

