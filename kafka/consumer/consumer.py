from kafka import KafkaConsumer
import json
import os

def json_deserializer(data):
    return json.loads(data.decode("utf-8"))

consumer = KafkaConsumer(
    "test_topic",
    bootstrap_servers=[os.getenv('KAFKA_BOOTSTRAP_SERVERS')],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    group_id='consumer-group',
    value_deserializer=json_deserializer
)

if __name__ == "__main__":
    for message in consumer:
        print(f"Received: {message.value}")
        consumer.commit()
