import requests
"""
#get
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
print(response.json())

#get using some specific params
url2 = "https://jsonplaceholder.typicode.com/posts/"
payload={
    "id":[1,2,3],
    "userID":1
}
response = requests.get(url2,params=payload)
res = response.json()
for i  in res:
    print(i,"\n")

#post 
url_post = "https://jsonplaceholder.typicode.com/posts"

new_data={
    "userId":1,
    "id":1,
    "title":"Making post request",
    "body":"This is the data i am uploading"
}

post_response = requests.post(url_post,json=new_data)
post_response_json = post_response.json()
print(post_response_json)

"""

#auth
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv
load_dotenv()

private_url = "https://api.github.com/user"
github_username = "shubham-affinsys"
token = os.getenv("TOKEN_GIT")

private_url_response = requests.get(
    url=private_url,
    auth=HTTPBasicAuth(github_username,token)
)

res=private_url_response.json()

name = res["name"]
login = res["login"]
id = res["id"]
url = res["url"]
bio = res["bio"]

print("anme: ",name)
print("Username: ",login)
print("id: ",id)
print("url: ",url)
print("bio: ",bio)