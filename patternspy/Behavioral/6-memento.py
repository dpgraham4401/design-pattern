# Memento Pattern
# A relatively simple pattern that allows us to rollback (undo) an object to a previous state
# Useful when you need to provide an undo action


class EditorMememto:
    def __init__(self, content):
        self.saved_content = content

    def get_content(self):
        return self.saved_content


class Editor:
    def __init__(self):
        self.content = ""

    def type(self, text):
        self.content = f"{self.content} {text}"

    def get_content(self):
        return self.content

    def save(self):
        return EditorMememto(self.content)

    def restore(self, save_point: EditorMememto):
        self.content = save_point.get_content()

    def __str__(self):
        return self.content


def main():
    """
    Here, we can create some content, save it, update it, and restore to teh original content.
    How cool is that!
    """
    editor = Editor()
    editor.type("Hello word\n")
    print("original content\n-------")
    print(editor)
    save = editor.save()
    editor.type("Luke, I am your father")
    print()
    print("updated Content\n-------")
    print(editor)
    editor.restore(save)
    print()
    print("restored content\n-------")
    print(editor)


if __name__ == "__main__":
    main()
