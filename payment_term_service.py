import signal
import json
import threading
import random
from payment_term_consumer import PaymentTermConsumer
from payment_term_producer import PaymentTermProducer


class PaymentTermService:
    """
    Consume messages from a ,
    process those messages to add price information,
    then publish them to another topic.
    """

    def __init__(self):
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        self.payment_term_consumer = PaymentTermConsumer()
        self.payment_term_producer = PaymentTermProducer()

    def start(self):
        print('Payment Term Service subscribing start')
        self.payment_term_consumer.subscribe(self.onMessage)
        print('Payment Term Service subscribing end')

    def stop(self, signalnum, handler):
        print('Stopping Payment Term Service')
        self.payment_term_consumer.close()
        self.payment_term_producer.close()

    def onMessage(self, message):
        print(message)
        self.process_payment_term(message.value)

    def process_payment_term(self, v):
        data = json.loads(v)
        payment_term_array = ['Letter of Credit', 'Advance Payment',
                              'Cash on Delivery', 'Open Account', 'Documentary Collection']
        shipping_order = {
            'shippingOrderId': data['shippingOrderId'],
            'customerName': data['customerName'],
            'purchaseOrderNumber': data['purchaseOrderNumber'],
            'shipFromCountryCode': data['shipFromCountryCode'],
            'shipToCountryCode': data['shipToCountryCode'],
            'shippingMethod': data['shippingMethod'],
            'shippingStatus': 'PAYMENT_TERM_ASSIGNED',
            'paymentTerm': random.choice(payment_term_array),
        }
        # Simulate a long processing time
        t = threading.Timer(5.0,
                            lambda: self.payment_term_producer.send(shipping_order))
        t.daemon = True
        t.start()
