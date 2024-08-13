import pika
import sys,time

for i in range(1, 100):
    # time.sleep(2)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue2', durable=True)

    in_msg = ' '.join(sys.argv[1:])
    msg = f"{in_msg} ...count:-> {i}"

    channel.basic_publish(exchange='',
                          routing_key='task_queue2',
                          body=msg,
                          properties=pika.BasicProperties(
                              delivery_mode=pika.DeliveryMode.Persistent  # persistence not fully granted
                          ))  # add properties to make msg more durable
    print(f" [x] message sent count--> {i}")
    connection.close()

"""
ROUND ROBBIN DISPATCHING
by default if we make 2 subs (worker.py) of same new_task pub
it will perform round robin - send each msg to next customer in sequence and on average every cust will get same no of msg

Doing a task can take a few seconds, you may wonder what happens if a consumer starts a long task and it terminates before it completes. With our current code once RabbitMQ delivers message to the consumer, it immediately marks it for deletion. In this case, if you terminate a worker, the message it was just processing is lost. The messages that were dispatched to this particular worker but were not yet handled are also lost.
But we don't want to lose any tasks. If a worker dies, we'd like the task to be delivered to another worker.
In order to make sure a message is never lost, RabbitMQ supports message acknowledgments. An ack(acknowledgement) is sent back by the consumer to tell RabbitMQ that a particular message had been received, processed and that RabbitMQ is free to delete it.


ex.

# shell 1
python worker.py
# => [*] Waiting for messages. To exit press CTRL+C

# shell 2
python worker.py
# => [*] Waiting for messages. To exit press CTRL+C

# shell 3
python new_task.py First message.
python new_task.py Second message..
python new_task.py Third message...
python new_task.py Fourth message....
python new_task.py Fifth message.....


# shell 1
python worker.py
# => [*] Waiting for messages. To exit press CTRL+C
# => [x] Received 'First message.'
# => [x] Received 'Third message...'
# => [x] Received 'Fifth message.....'

# shell 2
python worker.py
# => [*] Waiting for messages. To exit press CTRL+C
# => [x] Received 'Second message..'
# => [x] Received 'Fourth message....'

"""
