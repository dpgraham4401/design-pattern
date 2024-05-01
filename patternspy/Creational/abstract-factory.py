# Abstract Factory Pattern
# The abstract factory pattern is a method for creating related objects without specifying their concrete classes. It is
# a way to create a group of objects that each individually satisfy an interface.

# Generally, the abstract factory should implement an interface, and the objects it creates should also implement an
# interface. This way, the client code can use the abstract factory to create objects without needing to know the
# specific classes it's using. This is useful when the client code needs to create a group of related objects, but it
# doesn't need to know the specifics of how they're created.

from abc import ABC, abstractmethod
from time import sleep


class TableFactory(ABC):
    """The interface for making tables and related objects."""

    @abstractmethod
    def build_top(self):
        pass

    @abstractmethod
    def build_legs(self):
        pass


class Top(ABC):
    """The interface for table tops."""

    @abstractmethod
    def attach_legs(self, legs):
        pass


class Legs(ABC):
    """The interface for table legs."""

    @abstractmethod
    def repair(self):
        pass


class VictorianTableTop(Top):
    """A Victorian-style table-top."""

    def __init__(self):
        self.legs = None

    def attach_legs(self, legs):
        print(f"Attaching {legs} to the {self.__class__.__name__}.")
        self.legs = legs


class VictorianTableLegs(Legs):
    """Victorian-style table legs."""

    def repair(self):
        print("restoring the classy Victorian legs...")
        sleep(1)

    def __str__(self):
        return f"{self.__class__.__name__}"


class ContemporaryTableTop(Top):
    """A contemporary-style table-top."""

    def __init__(self):
        self.legs = None

    def attach_legs(self, legs):
        print(f"Attaching {legs} to the {self.__class__.__name__}table top.")
        self.legs = legs


class ContemporaryTableLegs(Legs):
    """Contemporary-style table legs."""

    def repair(self):
        print("repairing the modern legs...")
        sleep(1)

    def __str__(self):
        return f"{self.__class__.__name__}"


class ContemporaryTableFactory(TableFactory):
    """An abstract factory for creating contemporary tables and related objects."""

    def build_top(self):
        return ContemporaryTableTop()

    def build_legs(self):
        return ContemporaryTableLegs()


class VictorianTableFactory(TableFactory):
    """A factory for creating Victorian tables and related objects."""

    def build_top(self):
        return VictorianTableTop()

    def build_legs(self):
        return VictorianTableLegs()


def main():
    """
    Just remember -> abstract factory means were abstracting the concrete classes. Now the client code (below) doesn't
    know anything about what specific classes it's using, only that they satisfy the interface (TableFactory, Top, Legs)
    It also helps us pair inter-related objects together (we don't want to attach Victorian legs to a contemporary top).
    """
    # Create a Victorian table
    victorian_factory = VictorianTableFactory()
    top = victorian_factory.build_top()
    legs = victorian_factory.build_legs()
    top.attach_legs(legs)
    legs.repair()

    # Create a contemporary table
    contemporary_factory = ContemporaryTableFactory()
    top = contemporary_factory.build_top()
    legs = contemporary_factory.build_legs()
    top.attach_legs(legs)
    legs.repair()


if __name__ == "__main__":
    main()
