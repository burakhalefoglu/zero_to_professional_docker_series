import pika
import os
import json

rabbitmq_host = os.getenv('RABBITMQ_HOST', 'localhost')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

channel.queue_declare(queue='test_queue')

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Received: {message}")

channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
