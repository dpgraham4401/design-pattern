# Iterator Pattern
# Simple but classic! The iterator pattern access the elements of an aggregate object sequentially without exposing its
# underlying presentation. For example, we could iterate over an array, hash map, whatever.
# We see this pattern all the time with built-in iterables and iterators in various languages.
from collections.abc import Iterator


# In idiomatic Python, we have the __iter__, __next__, and the __getitem__ dunder methods.
# The __iter__ method returns an iterator object, and the __next__ method returns the next element in the sequence,
# and the __getitem__ method allows us to access elements by index.


class Book:
    """Book is a simple class that holds a title"""

    def __init__(self, title: str):
        self.title = title

    def __str__(self):
        return self.title


class BookIterator(Iterator):
    """
    Here's the magic! The iterator implements the __next__ method, and keeps state on the current location in
    the collection, with a reference to the iterable object.
    """

    def __init__(self, bookshelf: "BookShelve"):
        self._bookshelf = bookshelf
        self.index = 0

    def __next__(self):
        try:
            book = self._bookshelf[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return book


class BookShelve:
    """
    The BookShelve class is the aggregate object. It holds a collection of books, and provides an interface to iterate
    """

    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def __getitem__(self, index: int):
        return self._books[index]

    def __iter__(self):
        return BookIterator(self)


def main():
    """
    This is a simple example of the iterator pattern. We have a BookShelve that holds a collection of books.
    We can iterate over the books without knowing the details of the collection.
    """
    bookshelf = BookShelve()
    bookshelf.add_book(Book("The Alchemist"))
    bookshelf.add_book(Book("The Little Prince"))
    bookshelf.add_book(Book("The Art of War"))
    bookshelf.add_book(Book("The Catcher in the Rye"))
    bookshelf.add_book(Book("The Great Gatsby"))

    # Just like any other iterable, we can use a for loop to iterate over the collection.
    for book in bookshelf:
        print(book)


if __name__ == "__main__":
    main()
