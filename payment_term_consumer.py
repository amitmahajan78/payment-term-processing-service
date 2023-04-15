import os
import json
from kafka import KafkaConsumer
import constants as c


class PaymentTermConsumer:
    def __init__(self):

        self.consumer = KafkaConsumer(
            bootstrap_servers=os.getenv('KAFKA_BOOTSTRAP_SERVER'),
            group_id=c.CONSUMER_GROUP_ID,
            api_version=(0, 10, 2))

    def subscribe(self, onMessage):
        self.consumer.subscribe([c.PAYMENT_TERM_CONSUMER_TOPIC])
        print(f'Subscribed to "{c.PAYMENT_TERM_CONSUMER_TOPIC}"')

        for message in self.consumer:
            onMessage(message)
