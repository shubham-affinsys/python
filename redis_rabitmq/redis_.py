# import redis
# r = redis.Redis(host='localhost', port=6379, db=0, protocol=3)
# r.set('foo','bar')
# r.get('foo')
"""
connection pool:
pool= redis.ConnectionPool(host="localhost",port=6379, db=0)
r = redis.Redis(connection_pool=pool)
"""

import redis

r = redis.Redis()
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

print(r.get("Bahamas"))  # fn returns in bytes
print(r.get("Bahamas").decode('utf-8'))

# Allowed keys
# bytes str int or float -> they are converted to bytes before sending them to server as keys
# other we need to explicitly need to convert
# ex

import datetime

today = datetime.date.today().isoformat()
visitors = {"dan", "jon", "alex"}

# sass: set-add
r.sadd(today, *visitors)  # set or add key-value pair # returns  no of inserted element

print(r.smembers(today))  # returns value
print(r.scard(today))