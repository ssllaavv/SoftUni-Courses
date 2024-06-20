class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f"Book: {self.title} by {self.author}, page {self.page}."


class Library:

    LOCATION = 1

    def __init__(self):
        self.books = dict()

    def add_books(self, *books):
        for book in books:
            if book not in self.books:
                self.books[book] = Library.LOCATION
                Library.LOCATION += 1

    def find_book(self, title):
        for b in self.books.keys():
            if b.title == title:
                return f"Book: {str(b)}\n Location: {self.books[b]}"
        return f"Book {title} not found"


b1 = Book("First book", "First author")
b2 = Book("First book", "First author")
b3 = Book("First book", "First author")
b4 = Book("Second book", "Second author")
b5 = Book("Second book", "Second author")
b6 = Book("Third book", "Third author")
b7 = Book("Fourth book", "Fourth author")
b8 = Book("Fifth book", "Fifth author")

b1.turn_page(9)
b2.turn_page(90)
b4.turn_page(22)
b5.turn_page(234)
b5.turn_page(11)

l = Library()

l.add_books(b8, b7, b6, b5, b4, b3, b2, b1)

print(l.books)

print(l.find_book("First book"))
print(l.find_book("Second book"))


