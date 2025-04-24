import json
import time
from kafka import KafkaProducer
from faker import Faker

fake = Faker()

BOOTSTRAP_SERVERS = "localhost:9092"
TOPIC = "transactions"

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode()
)

def generate_transaction():
    return {
        "id": fake.uuid4(),
        "user_id": fake.uuid4(),
        "amount": round(fake.random_number(digits=4) / 100, 2),
        "merchant": fake.company(),
        "timestamp": fake.iso8601(),
    }

if __name__ == "__main__":
    while True:
        txn = generate_transaction()
        producer.send(TOPIC, txn)
        print(f"sent: {txn['id']}")
        time.sleep(1)