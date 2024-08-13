import redis
import sys

if len(sys.argv) == 2:
    program, action = sys.argv
    channel = "shubh"
    client = redis.Redis(host='localhost', port=6379)
    client.publish(channel, action)
else:
    print("You must give action(what you want to publish)")
