from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode()),
    group_id="fraud-detector-group"
)

for msg in consumer:
    txn = msg.value
    print(f"received: {txn['id']}")