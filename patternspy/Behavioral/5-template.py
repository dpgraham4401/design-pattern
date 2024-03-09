# Template pattern
# Behavioral pattern that lets us define the blueprint for executing an algorithm, but allows subclasses to override
# specific steps.

from abc import ABC, abstractmethod

database = {
    "users": {
        "admin1": "password1",
        "user2": "password2",
        "user3": "password3",
    },
    "roles": {
        "admin1": "admin",
        "user2": "user",
        "user3": "user",
    },
}


class Request:
    def __init__(self, username: str, password: str, headers=None):
        if headers is None:
            headers = {}
        self.username = username
        self.password = password
        self.headers = headers


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


class MiddleWareProcessor(ABC):
    @abstractmethod
    def run_middleware(self, request: Request) -> bool:
        pass


class HttpRequestProcessor(ABC):
    """
    The Template class
    """

    def __init__(self, middleware: [MiddleWareProcessor] = None):
        if middleware is None:
            middleware = []
        self.middleware = middleware

    @abstractmethod
    def authenticate(self, request) -> bool:
        pass

    @abstractmethod
    def authorize(self, request) -> bool:
        pass

    def process(self, request: Request) -> bool:
        """
        A method that accepts a request and returns true if the request is authenticated, authorized, and
        (conceivably) any other middleware added.
        """
        middleware_result = True
        for middleware in self.middleware:
            if not middleware.run_middleware(request):
                middleware_result = False
                break
        authenticated = self.authenticate(request)
        authorized = self.authorize(request)
        return authorized and authenticated and middleware_result


class AdminRequestProcessor(HttpRequestProcessor):
    def authenticate(self, request: Request) -> bool:
        try:
            return request.password == database["users"][request.username]
        except KeyError:
            return False

    def authorize(self, request: Request) -> bool:
        try:
            return database["roles"][request.username] == "admin"
        except KeyError:
            return False


class MyCustomTokenMiddleware(MiddleWareProcessor):
    def run_middleware(self, request: Request):
        try:
            return request.headers["token"] is not None
        except KeyError:
            return False


def main():
    # The requests to be processed
    admin_request = Request(username="admin1", password="password1")
    user_request = Request(username="user2", password="password2")
    admin_request_with_token = Request(
        "admin1", password="password1", headers={"token": "my_token"}
    )

    # Middleware
    token_middleware = MyCustomTokenMiddleware()

    # Implementation of the template
    http_processor = AdminRequestProcessor()
    admin_processor_with_mid = AdminRequestProcessor([token_middleware])

    # Results and processing
    print("Admin Request: ", http_processor.process(admin_request))
    print("Non-admin Request: ", http_processor.process(user_request))
    print("Admin Without token", admin_processor_with_mid.process(admin_request))
    print(
        "Admin With token", admin_processor_with_mid.process(admin_request_with_token)
    )


if __name__ == "__main__":
    main()
