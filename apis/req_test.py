import requests
import time
payload = {
        'method': 'GET',
        'headers': {
          'Authorization': 'token 9962edaa0003ac29e71e0972963544ae828e44db',
          'Content-Type': 'application/json',
        }
    }

base_url = 'https://my-dj.vercel.app/vege/recipes/';

for i in range(10):
    start = time.time()
    try:
        response = requests.get(base_url,payload)
        print("success")
    except Exception as e :
        print("failed")
    end = time.time()
    print("time taken:",end-start)
