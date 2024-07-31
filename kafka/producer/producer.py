from kafka import KafkaProducer
import json
import time
import os

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(
    bootstrap_servers=[os.getenv('KAFKA_BOOTSTRAP_SERVERS')],
    value_serializer=json_serializer,
    acks='all',
    retries=5
)

if __name__ == "__main__":
    while True:
        message = {"number": time.time()}
        producer.send("test_topic", message)
        print(f"Sent: {message}")
        time.sleep(1)