class Book:
    total_books = 0

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        Book.total_books += 1

    def __str__(self):
        return f"Title: {self.title}, ISBN: {self.isbn}"

    def __repr__(self):
        return f"Book(title='{self.title}', isbn='{self.isbn}')"

    def __eq__(self, other):
        return isinstance(other, Book) and other.isbn == self.isbn

    def __hash__(self):
        return hash((self.isbn))

    @staticmethod
    def is_valid(isbn):
        return isbn != ""

    @classmethod
    def from_string(cls, s):
        title, isbn = s.split("|")
        return cls(title,isbn)


    @property
    def short_title(self):
        return self.title[0:10]






