# Chain of Responsibility Pattern
# Used to pass requests along a chain of handlers until a suitable handler is found to process the request.
# useful when we need to build a fallback mechanism for a request, or we have a hierarchy of handlers.

class BaseAccount:
    def __init__(self, balance: float = 0):
        self.balance = balance
        self.successor = None

    def set_next(self, account: "BaseAccount"):
        self.successor = account
        return account

    def pay(self, amount: float):
        if self.can_pay(amount):
            print(f"Paid {amount} using {self.__class__.__name__}")
        elif self.successor:
            print(f"Can't pay using {self.__class__.__name__}. Passing request to {self.successor.__class__.__name__}")
            self.successor.pay(amount)
        else:
            print(f"None of the accounts have enough balance to pay {amount}")

    def can_pay(self, amount: float) -> bool:
        return self.balance >= amount


class BankAccount(BaseAccount):
    pass


class AccountCredit(BaseAccount):
    pass


class PayPalAccount(BaseAccount):
    pass


def main():
    """
    Say we have a client account, first we try to pay with the account credit, if it doesn't have enough balance,
    we move down the chain of accounts to the next one, and so on.
    """
    account = AccountCredit(100)
    paypal = PayPalAccount(200)
    bank = BankAccount(300)
    account.set_next(paypal)
    paypal.set_next(bank)
    account.pay(250)


if __name__ == "__main__":
    main()
