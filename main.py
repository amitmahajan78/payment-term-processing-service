from payment_term_service import PaymentTermService


def main():
    print('Starting Payment Term Service...')
    service = PaymentTermService()
    service.start()


if __name__ == '__main__':
    print("Starting app version 1.0")
    main()
