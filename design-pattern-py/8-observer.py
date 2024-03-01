# Observer pattern
from abc import ABC, abstractmethod


# a behavioral design pattern that allows object(s) to subscribe to changes in state of another object
# The 'subject' maintains a list of 'observers' and notifies them, usually through a method call, of state changes

class Stock:
    """Subject class that maintains a list of observers and notifies them of state changes."""

    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.observers = []

    def change_price(self, price):
        self.price = price
        self.notify()

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.notify(self)


class Subscriber(ABC):
    """The interface for the observer to be notified of state changes."""

    @abstractmethod
    def notify(self, stock: Stock):
        pass


class Investor(Subscriber):
    """Observer that subscribes to subject state changes"""

    def __init__(self, name):
        self.name = name

    def notify(self, stock: Stock):
        print(f'Notified {self.name} of {stock.symbol}\'s price change to {stock.price}')


def main():
    # The Subject
    stock = Stock('OXY', 1000)
    # The Observers
    investor1 = Investor('Dmoney')
    investor2 = Investor('Daddy Warbucks')

    stock.attach(investor1)
    stock.attach(investor2)

    stock.change_price(1130)
    stock.change_price(1345)

    stock.detach(investor1)
    stock.change_price(998)


if __name__ == '__main__':
    main()
