import redis
import json
import ast

redis_client = redis.Redis(host="localhost", port=6379, db=4)

redis_client.set("username", "shubh", 10)

username = redis_client.get("username").decode('utf-8')
# print(username)

user_data = {"name": "shubham", "team": "SE"}
redis_client.set(username, json.dumps(user_data))  # the dict converted to str then sent as bytes

usr_data = redis_client.get(username).decode('utf-8')
usr_data = ast.literal_eval(usr_data)  # convert str to dict

print("username:", username)
print("user data -->")
for key, val in usr_data.items():
    print(key, ":", val)
