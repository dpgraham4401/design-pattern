# Adapter pattern
# The Adapter pattern lets us make an incompatible object compatible with another class.
# For example, we have class A, B, and C; A and C are incompatible with each other ( C does not
# meet the interface expected by A). We can create the adapter class B to make C compatible with A.
from abc import ABC, abstractmethod
from typing import TypedDict


# The adapter pattern is a structural pattern, the pattern category that is primarily concerned with how objects
# fit together.

class Position(TypedDict):
    x: int
    y: int


class Animal(ABC):
    def __init__(self, position: Position | None = None):
        self.position = position if position else Position(x=0, y=0)


class Mammal(Animal):
    @abstractmethod
    def move(self, position: Position):
        pass


class Bird(Animal):
    @abstractmethod
    def fly(self, position: Position):
        pass


class Dog(Mammal):
    """The Dog/Mammal class has a move method. as expected by the client code. No adapter is needed."""

    def move(self, position: Position):
        print(f"Dog is walking to {position}")
        self.position = position


class Parrot(Bird):
    """
    The Parrot/Bird class has a fly method instead of the move method.
    An adapter is needed to make it compatible with the client code, and satisfy the Mammal interface.
    """

    def fly(self, position: Position):
        print(f"Parrot is flying to {position}")
        self.position = position


def move_animal(animal: Mammal, position: Position):
    """The move_animal function expects the animal object to have the move method (satisfying the Mammal interface)"""
    animal.move(position)


class BirdAdapter(Mammal):

    def __init__(self, bird: Bird):
        super().__init__(bird.position)
        self.bird = bird

    def move(self, position: Position):
        self.bird.fly(position)


def main():
    dog = Dog()
    parrot = Parrot()
    parrot_adapter = BirdAdapter(parrot)
    move_animal(dog, Position(x=10, y=10))
    move_animal(parrot_adapter, Position(x=30, y=45))


if __name__ == "__main__":
    main()
