# Builder Pattern
# allows constructing different flavors of complex objects step by step


class GolfSet:
    def __init__(self):
        self.title = None
        self.putter = None
        self.driver = None
        self.three_wood = None
        self.nine_iron = None
        self.eight_iron = None
        self.seven_iron = None
        self.six_iron = None
        self.five_iron = None

    # The builder pattern allows us to chain methods together
    # the secret is that each method returns the object itself
    def add_title(self, title: str = None):
        self.title = title if title else "My Golf Set"
        return self

    def add_putter(self, putter: str = None):
        self.putter = putter if putter else "Default Putter"
        return self

    def add_driver(self, driver: str = None):
        self.driver = driver if driver else "Default Driver"
        return self

    def add_three_wood(self, three_wood: str = None):
        self.three_wood = three_wood if three_wood else "Default Three Wood"
        return self

    def add_nine_iron(self, nine_iron: str = None):
        self.nine_iron = nine_iron if nine_iron else "Default Nine Iron"
        return self

    def add_eight_iron(self, eight_iron: str = None):
        self.eight_iron = eight_iron if eight_iron else "Default Eight Iron"
        return self

    def add_seven_iron(self, seven_iron: str = None):
        self.seven_iron = seven_iron if seven_iron else "Default Seven Iron"
        return self

    def add_six_iron(self, six_iron: str = None):
        self.six_iron = six_iron if six_iron else "Default Six Iron"
        return self

    def add_five_iron(self, five_iron: str = None):
        self.five_iron = five_iron if five_iron else "Default Five Iron"
        return self

    def __str__(self):
        title = f"{self.title}\n"
        separator = "-" * len(title) + "\n"
        return "\n" + title + separator + "\n".join(
            [f"{attr.replace("_", " ").capitalize()}: {value}" for attr, value in vars(self).items() if
             value is not None])


def main():
    """
    Instead of passing a bunch of arguments to the constructor,
    we can use the builder pattern to add the clubs we want.
    """
    my_golf_set = (GolfSet()
                   .add_title("My Golf Set")
                   .add_driver()
                   .add_putter()
                   .add_three_wood()
                   .add_nine_iron()
                   .add_six_iron())
    print(my_golf_set)
    my_friends_golf_set = (GolfSet()
                           .add_title("My Friend's Set")
                           .add_putter("Ping Putter")
                           .add_three_wood("TaylorMade Three Wood")
                           .add_nine_iron("Ping Nine Iron")
                           .add_seven_iron()
                           .add_six_iron())
    print(my_friends_golf_set)


if __name__ == "__main__":
    main()
