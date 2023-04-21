import os
import json
from kafka import KafkaConsumer
import constants as c


class PaymentTermConsumer:

    def __init__(self):
        print(os.environ.get('BOOTSTRAP_SERVERS'))
        print(os.environ.get('SASL_MECHANISM'))
        print(os.environ.get('SECURITY_PROTOCOL'))
        print(os.environ.get('SASL_USERNAME'))
        print(os.environ.get('SASL_PASSWORD'))

        self.consumer = KafkaConsumer(bootstrap_servers=[os.environ.get('BOOTSTRAP_SERVERS')],
                                      sasl_mechanism=os.environ.get(
                                          'SASL_MECHANISM'),
                                      security_protocol=os.environ.get(
                                          'SECURITY_PROTOCOL'),
                                      sasl_plain_username=os.environ.get(
                                          'SASL_USERNAME'),
                                      sasl_plain_password=os.environ.get(
                                          'SASL_PASSWORD'),
                                      group_id='Payment_Term_Service',
                                      auto_offset_reset='earliest',)

    def subscribe(self, onMessage):
        self.consumer.subscribe(["shipping_order_created"])
        print("subscribe to shipping_order_created")
        for message in self.consumer:
            print(message)
            onMessage(message)
