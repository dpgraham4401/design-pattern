# Flyweight pattern
#
# A pattern used to minimize memory usage for computationally expensive operations or when you have a
# large number of instances of a class.
#
# The classic example is a text editor, with infinite memory we could store each character in a separate object. That
# object would hold the state of the character's font, size, etc.
#
# To save memory, we separate intrinsic state, shared between objects (it's the letter 'a'), and extrinsic state, unique
# to each object (the font and size of the letter 'a').
from typing import TypedDict


class Character:
    def __init__(self, character):
        self.character = character

    def __str__(self):
        return f'Character: {self.character}'

    def __repr__(self):
        """shows the class and memory location"""
        return f'{self.__class__.__name__}({self.character}, {hex(id(self))})'


class CharacterFlyweightFactory:
    """Flyweight factory that maintains a pool of flyweight objects."""

    characters = {}

    def __init__(self, initial_characters=None):
        if initial_characters is None:
            initial_characters = {}
        self.characters = initial_characters

    def get_character(self, character):
        """Return a character from the pool if it exists, otherwise create a new one."""
        if character not in self.characters:
            self.characters[character] = Character(character)
        return self.characters[character]

    def __str__(self):
        return f'{[char for char in self.characters]}'


class CharacterInstance(TypedDict):
    character: Character
    font: str
    size: int


class Document:
    def __init__(self):
        self.characters: [CharacterInstance] = []

    def add_character(self, factory: CharacterFlyweightFactory, character, font: str, size: int):
        self.characters.append((factory.get_character(character), font, size))

    def __repr__(self):
        """returns a multiline string of all the characters in the document and their font and size"""
        return '\n'.join(
            [
                f'{repr(char[0])}, Font: {char[1]}, Size: {char[2]}'
                for char in self.characters])


def main():
    """
    Now we can add multiple letter 'A's to the document, the document only has to store extrinsic state (font and size)
    for each character, the intrinsic state (the character itself) is shared between all instances.
    as proven by the memory location of the character objects.
    """
    factory = CharacterFlyweightFactory({'a': Character('a'), 'b': Character('b')})
    print('initial available characters ', factory)
    doc = Document()

    # as the users types characters, we use the flyweight factory to add them to the document
    doc.add_character(factory, 'a', 'times', 12)  # 'a' is in the factory, so it will be reused
    doc.add_character(factory, 'a', 'calibre', 10)  # 'a' is in the factory, so it will be reused
    doc.add_character(factory, 'b', 'arial', 10)  # 'b' is in the factory, so it will be reused
    doc.add_character(factory, 'c', 'times', 10)  # 'c' is not in the factory, so it will be added

    print('The Document\n-------------------')
    print(doc)
    print('-------------------')
    print('final available characters ', factory)

    # Example output:
    # initial available characters  ['a', 'b']
    # The Document
    # -------------------
    # Character(a, 0x100a22de0), Font: times, Size: 12
    # Character(a, 0x100a22de0), Font: calibre, Size: 10
    # Character(b, 0x100a22db0), Font: arial, Size: 10
    # Character(c, 0x100a38470), Font: times, Size: 10
    # -------------------
    # final available characters  ['a', 'b', 'c']


if __name__ == '__main__':
    main()
