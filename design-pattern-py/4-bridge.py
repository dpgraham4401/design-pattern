# Bridge Pattern
# allows us to decouple an abstraction from its implementation so that the two can vary independently
from abc import ABC, abstractmethod


# The trick to the bridge pattern is we break apart a tree-like hierarchy into two parallel hierarchies
# so this tree:
#   A
#  / \
# B   C

# becomes two hierarchies:
#   A       N
#          / \
#         B   C
# Now A takes B or C as an instance member, and can call methods from an interface they both satisfy

class Theme(ABC):
    @abstractmethod
    def get_color(self) -> str:
        pass


class DarkTheme(Theme):
    def get_color(self) -> str:
        return "Black"


class LightTheme(Theme):
    def get_color(self) -> str:
        return "White"


class WebPage:
    def __init__(self, theme: Theme):
        self.theme = theme

    def set_theme(self, theme: Theme):
        self.theme = theme

    def get_content(self) -> str:
        return f"Content in {self.theme.get_color()}"


def main():
    """
    Now we can change the theme of the page without subclassing web page (many times) and we can change/add theme
    classes at will (so long as they satisfy the Theme interface)
    """
    dark_theme = DarkTheme()
    light_theme = LightTheme()

    page = WebPage(light_theme)
    print(page.get_content())

    page.set_theme(dark_theme)
    print(page.get_content())


if __name__ == "__main__":
    main()
