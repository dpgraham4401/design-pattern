# Command pattern
# The command pattern is a behavioral design pattern designed to decouple the client from the receiver through
# an invoker. The 'invoker' takes the 'command' from a 'client', and passes it to the 'receiver' to execute it.

from abc import ABC, abstractmethod


# The command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Robot:
    def __init__(self):
        self.position = 0

    def move_forward(self):
        self.position += 1
        print("moving forward")

    def move_backward(self):
        self.position -= 1
        print("moving backward")

    def __str__(self):
        return f"Robot position: {self.position}"


class MoveForward(Command):
    def __init__(self, robot):
        self.robot = robot

    def execute(self):
        self.robot.move_forward()


class MoveBackward(Command):
    def __init__(self, robot):
        self.robot = robot

    def execute(self):
        self.robot.move_backward()


class RemoteControl:
    @staticmethod
    def press_button(command):
        command.execute()


def main():
    robot = Robot()
    move_forward = MoveForward(robot)
    move_backward = MoveBackward(robot)

    print(robot)
    # The client presses the button to move the robot forward X times
    RemoteControl.press_button(move_forward)
    RemoteControl.press_button(move_forward)
    RemoteControl.press_button(move_forward)
    print(robot)
    # To move backwards, just pass the move_backward instance to the RemoteControl
    RemoteControl.press_button(move_backward)
    print(robot)


if __name__ == "__main__":
    main()
