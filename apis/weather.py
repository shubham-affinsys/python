import requests

API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "3805f6bbabcb42b3a0c08a489baf603d"

params = {
    "country":"us",
    "apiKey":API_KEY
}

response = requests.get(API_URL,params=params)

if response.status_code == 200:
    data = response.json()
    

else:
    print(f"Error: {response.status_code}")