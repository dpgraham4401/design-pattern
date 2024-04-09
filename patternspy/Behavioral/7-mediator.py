# Mediator Pattern
# a behavioral pattern that defines an object that encapsulates how a set of objects interact.
# I generally think of it like, I have a single object that you provide to multiple consumer objects then they each
# interact with that single object to communicate with each other.
from abc import ABC, abstractmethod


class ChatRoomMediator(ABC):
    @abstractmethod
    def display_messages(self):
        pass

    @abstractmethod
    def send_message(self, user, message):
        pass


class ChatRoom(ChatRoomMediator):
    def __init__(self):
        self.users = []
        self.messages = []

    def display_messages(self):
        for message in self.messages:
            print(message)

    def send_message(self, user: "User", message: str):
        self.messages.append(f"{user}: {message}")


class User:
    def __init__(self, name: str, chat_room: ChatRoomMediator):
        self.name = name
        self.chat_room = chat_room

    def send_message(self, message: str):
        self.chat_room.send_message(self.name, message)

    def __str__(self):
        return self.name


def main():
    chat_room = ChatRoom()
    david = User("David", chat_room)
    kelly = User("Kelly", chat_room)
    david.send_message("Hey Kelly!")
    kelly.send_message("What up David!")
    chat_room.display_messages()


if __name__ == "__main__":
    main()
