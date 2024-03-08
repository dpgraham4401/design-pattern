# Strategy pattern
# A relatively simple pattern that allows us to change the behavior of an object at runtime by changing the strategy
# object. It's easy to tell when the strategy pattern is being used. Look for classes (the context)
# that have nested objects doing the work with a setter to interchange that object (the strategy).
from abc import abstractmethod, ABC


class Sorter(ABC):
    @abstractmethod
    def sort(self, data: list[int]):
        pass


class BubbleSort(Sorter):
    """
    Our bubble sort strategy.
    Generally bad for large data sets, but easy to implement and understand.
    """

    def sort(self, data: list[int]):
        for i in range(1, len(data)):
            for n in range(0, len(data) - i):
                if data[n] > data[n + 1]:
                    data[n], data[n + 1] = data[n + 1], data[n]
        return data


class InsertionSort(Sorter):
    """
    Insertion quick sort strategy implementation.
    """

    def sort(self, data: list[int]):
        for step in range(1, len(data)):
            key = data[step]
            j = step - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j = j - 1
            data[j + 1] = key
        return data


class ClientContext:
    """
    This (poorly named) class is the context for the strategy pattern.
    It's the client code that uses the strategy.
    """

    def __init__(self):
        self._strategy: Sorter | None = None

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Sorter):
        self._strategy = strategy

    def sort(self, data: list[int]):
        return self.strategy.sort(data)


def main():
    ctx = ClientContext()
    ctx.strategy = BubbleSort()

    data1 = [1, 3, 6, 2, 4, 1, 9, 5]
    print("data ", data1)
    bubble_sorted_data = ctx.sort(data1)
    print("bubble sort ", bubble_sorted_data)
    ctx.strategy = InsertionSort()
    insertion_sorted_data = ctx.sort(data1)
    print("insertion sort ", insertion_sorted_data)


if __name__ == "__main__":
    main()
