# Prototype Pattern
# Used to create new objects by copying an existing object (known as the prototype). IMO, This pattern is useful when
# creating a new object is complex or expensive, or we'd like to use information in an existing object to create a new.
import copy


# In this example, I'm exploring the prototype pattern AND the copy module, and it's dunder methods.


class WasteHandler:
    """
    This is a concept from the waste management industry (from work). A waste handler a company that handles waste
    in the chain of custody. This could be a generator, transporter, or disposal facility (not important for now).
    """

    def __init__(self, epa_id: str, name: str):
        self.epa_id = epa_id
        self.name = name

    def __str__(self):
        return f"Handler: {self.epa_id}"

    def __repr__(self):
        return f"WasteHandler({self.epa_id}) at {hex(id(self))}"


class Manifest:
    """
    This is a concept from the waste management industry (from work). The manifest is a document that accompanies
    hazardous waste shipments from a generator -> transporter -> disposal facility.
    """

    def __init__(self, mtn: str, version: int = 1, generator: WasteHandler = None):
        self.mtn = mtn
        self.version = version
        self.generator = generator

    def set_generator(self, generator: WasteHandler):
        self.generator = generator

    def __str__(self):
        return f"Manifest: {self.mtn}"

    def __repr__(self):
        return f"Manifest: {self.mtn}\nVersion: {self.version}\nMem Loc: {hex(id(self))}\nGenerator {repr(self.generator)}"

    def __copy__(self):
        """
        This piece of Pythonic piece is the shallow __copy__ method. Called from copy.copy()
        A shallow copy creates a new object, but inserts references to any nested objects found in the original.
        """
        return Manifest(self.mtn, self.version + 1, generator=self.generator)


def main():
    """
    The original manifest automatically has version 1. Pretend it has a complex setup process.
    """
    generator = WasteHandler("VATESTGEN001", "Generator")
    manifest = Manifest("123456789ELC", generator=generator)

    print("\n----------\nOld Manifest")
    print(repr(manifest))  # should show the prototype manifest with version == 1

    # The new manifest doesn't need to know how to instantiate the WasteHandler or know details on the manifest.
    # We also automagically increment the version number.
    new_manifest = copy.copy(manifest)

    # If we implemented the __deepcopy__ method, we could use copy.deepcopy() which would instantiate new objects
    # for all nested objects (recursively).

    print("\n----------\nNew Manifest")
    print(
        repr(new_manifest)
    )  # new, identical instance to the prototype, but with version == 2
    # and a reference to the same generator object


if __name__ == "__main__":
    main()
