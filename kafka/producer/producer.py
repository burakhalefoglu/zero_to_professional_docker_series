from kafka import KafkaProducer
import json
import time
import os, logging

logging.basicConfig(level=logging.DEBUG)


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(
    bootstrap_servers=[os.getenv('KAFKA_BOOTSTRAP_SERVERS')],
    value_serializer=json_serializer,
    acks='all',
    retries=5
)
i=0
while True:
    message = {"number": str(time.time()) +" " + str(i)}
    i = i + 2
    future = producer.send("test_topic", message, partition=0)
    try:
        record_metadata = future.get(timeout=10)
        logging.info(f"Sent: {message} to {record_metadata.topic} partition {record_metadata.partition} offset {record_metadata.offset}")
    except Exception as e:
        logging.error(f"Failed to send message: {e}")
    time.sleep(5)