import redis
import sys

channel = "shubh"

client = redis.Redis(host="localhost", port=6379)
c = client.pubsub()
c.subscribe("shubh")

print("Subscribed to channel:", channel)
while True:
    try:
        msg = c.get_message()
        if msg and msg['data'] != 1:
            msg = msg["data"].decode('utf-8')
            print(msg)

    except KeyboardInterrupt:
        print("Intruded")
        sys.exit(0)