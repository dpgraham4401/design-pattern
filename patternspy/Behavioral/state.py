# State behavioral design pattern

# relatively simple pattern that allows us to change the implementation/behavior of an object at runtime.
# We store different implementations in the object and call the methods of the implementation that we want to use.

from abc import ABC, abstractmethod


class LaptopState(ABC):
    @abstractmethod
    def power_button(self):
        pass

    @abstractmethod
    def volume_up_button(self):
        pass

    @abstractmethod
    def volume_down_button(self):
        pass

    @abstractmethod
    def type_words(self):
        pass


class LaptopOff(LaptopState):
    def power_button(self):
        print("Turning on laptop")
        return LaptopOn()

    def volume_up_button(self):
        print("Can't turn volume up, laptop is off")

    def volume_down_button(self):
        print("Can't turn volume down, laptop is off")

    def type_words(self):
        print("Can't type words, laptop is off")


class LaptopOn(LaptopState):
    def power_button(self):
        print("Turning off laptop")
        return LaptopOff()

    def volume_up_button(self):
        print("Turning volume up")

    def volume_down_button(self):
        print("Turning volume down")

    def type_words(self):
        print("Typing words")


class Laptop:
    def __init__(self):
        self.state = LaptopOff()

    def power_button(self):
        self.state = self.state.power_button()

    def volume_up_button(self):
        self.state.volume_up_button()

    def volume_down_button(self):
        self.state.volume_down_button()

    def type_words(self):
        self.state.type_words()


def main():
    # Client code
    laptop = Laptop()  # Laptop is off
    laptop.volume_up_button()
    laptop.volume_down_button()
    laptop.type_words()
    # Turning on laptop
    laptop.power_button()
    laptop.volume_up_button()
    laptop.volume_down_button()
    laptop.type_words()


if __name__ == "__main__":
    main()
