# Facade Pattern
# A facade provides a simple interface for an internally complex task
from abc import ABC, abstractmethod


class Dresser(ABC):
    """
    This is the interface for getting dressed
    """

    @abstractmethod
    def get_dressed(self):
        pass


class Attire(Dresser):
    """
    This class implements the Dresser interface and provides a simple interface for getting dressed.
    under the hood, getting dressed is an extremely complex task (lol), that requires putting on a shirt,
    pants, underwear, and socks.
    """

    def __init__(self):
        self.shirt = None
        self.pants = None
        self.underwear = None
        self.socks = None

    def get_dressed(self):
        self.put_on_shirt()
        self.put_on_pants()
        self.put_on_underwear()
        self.put_on_socks()

    def put_on_shirt(self):
        self.shirt = "polo"

    def put_on_pants(self):
        self.pants = "jeans"

    def put_on_underwear(self):
        self.underwear = "boxers"

    def put_on_socks(self):
        self.socks = "wool"

    def __str__(self):
        return f"Shirt: {self.shirt} Pants: {self.pants} Underwear: {self.underwear} Socks: {self.socks}"


def main():
    me = Attire()
    print("Getting dressed")
    print(me)
    me.get_dressed()
    print("Dressed!")
    print(me)


if __name__ == "__main__":
    main()
