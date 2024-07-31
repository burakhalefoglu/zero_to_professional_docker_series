import pika
import os
import json
import time

rabbitmq_host = os.getenv('RABBITMQ_HOST', 'localhost')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

channel.queue_declare(queue='test_queue')

def publish_message():
    message = {'number': time.time()}
    channel.basic_publish(exchange='',
                          routing_key='test_queue',
                          body=json.dumps(message))
    print(f"Sent: {message}")

if __name__ == "__main__":
    while True:
        publish_message()
        time.sleep(1)
