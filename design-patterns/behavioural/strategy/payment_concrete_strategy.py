from payment_strategy import PaymentStrategy


class CardPayment(PaymentStrategy):
    def __init__(self, account_number, cvv):
        self.account_number = account_number
        self.cvv = cvv

    def pay(self, amount):
        print("Paying this much amount {} with credit card".format(amount))


class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print("Paying this much amount {} with bitcoin".format(amount))
