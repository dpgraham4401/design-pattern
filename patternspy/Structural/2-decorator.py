# Decorator Pattern
# allows adding new functionality to an object without altering its structure

# Define a decorator that accepts a class and adds a 'greet' method
def add_greeting(cls):
    def greet(self):
        return f"Hello, I am an instance of {cls.__name__}."

    setattr(cls, "greet", greet)
    return cls


@add_greeting
class Human:
    pass


# A decorator that accepts a function and wraps the returned contents in a http response
def http_response(func):
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
    return f"data processed successfully"


def main():
    bob = Human()
    print(bob.greet())

    print()
    print("-" * 50)
    print()

    print(process_data())


if __name__ == "__main__":
    main()
