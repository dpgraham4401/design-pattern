# Visitor pattern
# A behavioral pattern that allows us to separate an algorithm from an object structure on which it operates.
# It's not a pattern that gets used a lot because it is a bit complex and is limited in scope of applicability.

from abc import ABC, abstractmethod


# The abstract visitor interface
class Renderer(ABC):
    @abstractmethod
    def render_body(self, body: str):
        pass

    @abstractmethod
    def render_heading(self, heading: str):
        pass


# A concrete implementation of our visitor interface
class HtmlRenderer(Renderer):
    def render_body(self, body: str):
        return f"<body>{body}</body>"

    def render_heading(self, heading: str):
        return f"<h1>{heading}</h1>"


# Another concrete implementation of our visitor interface
class TextRenderer(Renderer):
    def render_body(self, body: str):
        return f"{body}"

    def render_heading(self, heading: str):
        return f"{heading}"


# The abstract element interface
# By convention the method is called 'accept'
class DocumentElement(ABC):
    @abstractmethod
    def accept(self, renderer: Renderer):
        pass


# A document can contain many elements, as long as they implement the element interface (DocumentElement)
class Document:
    def __init__(self, elements: [DocumentElement] = None):
        self.elements: [DocumentElement] = elements

    def add_element(self, element: DocumentElement):
        self.elements.append(element)

    def accept(self, renderer: Renderer):
        results = []
        for element in self.elements:
            results.append(element.accept(renderer))
        return results


# A concrete implementation of our element interface
class Body(DocumentElement):
    def __init__(self, body: str):
        self.body = body

    def accept(self, renderer: Renderer):
        return renderer.render_body(self.body)


# Another concrete implementation of our element interface
class Heading(DocumentElement):
    def __init__(self, heading: str):
        self.heading = heading

    def accept(self, renderer: Renderer):
        return renderer.render_heading(self.heading)


def main():
    # Create a list of elements
    elements = [
        Heading("This is the heading"),
        Body("This is the body"),
        Body("This is the body too"),
    ]

    # The same document can be rendered in multiple ways
    document = Document(elements)

    # Set up the available renderers
    html_renderer = HtmlRenderer()
    text_renderer = TextRenderer()

    # Render the document with each renderer visitor
    print(document.accept(html_renderer))
    print(document.accept(text_renderer))


if __name__ == "__main__":
    main()
