#import Book
from Book import Book

def main():
    book1 = Book("Book1", 123)
    book2 = Book("Book2", 123)

    books = set()
    books.add(book1)
    books.add(book2)
    print(len(books))
    print(book1)

if __name__ == "__main__":
    main()