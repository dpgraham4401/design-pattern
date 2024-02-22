class Door:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def __str__(self):
        return f"Door with Width: {self.width}, Height: {self.height}"


def make_door(width, height):
    """
    Simple factory function to create a door.
    The benefit of this approach is that we can
    add some logic to the creation of the door
    and the client code doesn't need to be aware
    of the class we're using or how to construct it.
    """
    return Door(width, height)


def main():
    door = make_door(100, 200)
    print(door)


if __name__ == "__main__":
    main()
