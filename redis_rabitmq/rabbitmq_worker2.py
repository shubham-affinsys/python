import pika, sys, os
import time


# manual msg ack

# debug basic_ack:
# sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    # channel.queue_declare(queue='hello')
    channel.queue_declare(queue='task_queue2', durable=True)  # increase durability , need to define new queue because

    # we have defined a queue hello that is not durable

    def callback(ch, method, properties, body):
        print(f"[x] Received message: {body.decode('utf-8')}")
        time.sleep(body.count(b'.'))  # fake busy
        print("[x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)  # added basic ack

    channel.basic_consume(queue='task_queue2', on_message_callback=callback)  # removed auto_ack
    print('[*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(' Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

"""
ROUND ROBIN - auto_ack 
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f" [X] Received message: {body.decode('utf-8')}")
        time.sleep(body.count(b'.'))  # sleep for the amount of time there are . in msg to fake busy work
        print("[X] Done")
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
"""
