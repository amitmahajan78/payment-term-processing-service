import os
import json
from kafka import KafkaProducer
import constants as c


class PaymentTermProducer:
    def __init__(self):

        self.producer = KafkaProducer(
            bootstrap_servers=os.getenv('KAFKA_BOOTSTRAP_SERVER'),
            # value_serializer=lambda x: x.encode("utf-8"),
            api_version=(0, 10, 2))

    def send(self, message):
        print(f'Sending message "{message}"')
        return self.producer.send(c.PAYMENT_TERM_PRODUCER_TOPIC, json.dumps(message).encode("utf-8"))
