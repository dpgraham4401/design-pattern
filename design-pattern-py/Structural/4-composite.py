# Composite Pattern
# A composite pattern is a structural design pattern that lets us compose small objects into complex structures
# and then work with these structures as if they were an individual objects. The composite pattern recommends that
# we use the same interface for both the individual objects and the complex objects.

from abc import ABC, abstractmethod


class ManifestUser(ABC):
    @abstractmethod
    def get_manifest_count(self) -> int:
        pass


class Site(ManifestUser):
    def __init__(self, manifest_count: int):
        self.manifest_count = manifest_count

    def get_manifest_count(self) -> int:
        return self.manifest_count


class Organization(ManifestUser):
    def __init__(self, sites: [ManifestUser]):
        self.sites = sites

    def get_manifest_count(self) -> int:
        return sum(site.get_manifest_count() for site in self.sites)


def main():
    """
    Using the composite pattern, we can create a complex objects like tree structure, and then implement the same
    interface on the individual objects and the complex objects. Then we can work with the complex
    objects as if they were simple objects, the client code does not need to know the difference,
    and we can use the implement recursive methods to traverse the complex objects.
    """
    site1 = Site(10)
    site2 = Site(20)
    site3 = Site(30)
    sub_org = Organization([site1, site2, site3])
    site4 = Site(40)
    site5 = Site(50)
    org = Organization([sub_org, site4, site5])
    # now we have a complex structure that looks like this tree structure:
    # org
    # |---sub_org
    # |   |---site1
    # |   |---site2
    # |   |---site3
    # |---site4
    # |---site5
    print(org.get_manifest_count())
    # Calling get_manifest_count() retrieves the sum of all the manifest counts in the complex structure.
    # How cool is that!!!


if __name__ == "__main__":
    main()
