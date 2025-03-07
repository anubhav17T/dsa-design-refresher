from payment_strategy import PaymentStrategy
from payment_concrete_strategy import CardPayment, BitcoinPayment


class ProcessPayment:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self,strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount=amount)


credit_card = CardPayment(account_number=123123, cvv=123123)
bitcoin = BitcoinPayment(wallet_address=12312323)

processor = ProcessPayment(strategy=credit_card)
processor.process_payment(amount=200)

processor.set_strategy(strategy=bitcoin)
processor.process_payment(amount=1)


