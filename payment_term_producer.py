import os
import json
from kafka import KafkaProducer
import constants as c


class PaymentTermProducer:
    def __init__(self):

        self.producer = KafkaProducer(bootstrap_servers=[os.environ.get('BOOTSTRAP_SERVERS')],
                                      sasl_mechanism=os.environ.get(
                                          'SASL_MECHANISM'),
                                      security_protocol=os.environ.get(
                                          'SECURITY_PROTOCOL'),
                                      sasl_plain_username=os.environ.get(
                                          'SASL_USERNAME'),
                                      sasl_plain_password=os.environ.get(
                                          'SASL_PASSWORD'),)

    def send(self, message):
        print(f'Sending message "{message}"')
        return self.producer.send("shipping_order_payment_term_assigned", json.dumps(message).encode("utf-8"))
