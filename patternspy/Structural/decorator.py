# Decorator Pattern
# allows adding new functionality to an object without altering its structure
# In python, a function is also an object, so decorators can be designed to be used with functions
from typing import Callable


# A decorator that adds a greet method to a class
def add_greeting(cls):
    def greet(self) -> str:
        return f"Hello, I am an instance of {cls.__name__}."

    setattr(cls, "greet", greet)
    return cls


# The Human class will have a greet method/attribute that was added by the decorator
@add_greeting
class Human:
    pass


# A, seemingly, more common use case for decorators is to wrap a function
# A decorator that accepts a function and wraps the returned contents in a http response
def http_response(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n{result}"

    return wrapper


# Adding a decorator to a function ensures that our process_data 'component' adheres to the
# Single Responsibility Principle (SRP) principle. The only reason that the function
# should change is if the business logic changes, not because we decide to send it
# via email instead of HTTP
@http_response
def process_data():
    return "data processed successfully"


def main():
    bob = Human()
    print(bob.greet())

    print()
    print("-" * 50)
    print()

    print(process_data())


if __name__ == "__main__":
    main()
