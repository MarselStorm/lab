class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, int) and value > 0:
            self._pages = value
        else:
            raise ValueError("Pages must be a positive integer")

    def __str__(self):
        return f"PaperBook: {self.name} by {self.author}, {self.pages} pages"

    def __repr__(self):
        return f"PaperBook('{self.name}', '{self.author}', {self.pages})"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if isinstance(value, float) and value > 0:
            self._duration = value
        else:
            raise ValueError("Duration must be a positive float")

    def __str__(self):
        return f"AudioBook: {self.name} by {self.author}, {self.duration} hours"

    def __repr__(self):
        return f"AudioBook('{self.name}', '{self.author}', {self.duration})"
