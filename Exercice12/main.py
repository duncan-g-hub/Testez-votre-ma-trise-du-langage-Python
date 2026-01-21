class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrowed = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        book = self._find_book(book_title, self.books)
        if book:
            self.books.remove(book)
        else:
            print(f"Le livre {book_title} n'est pas dans la bibliothèque.")

    def borrow_book(self, book_title):
        book = self._find_book(book_title, self.books)
        if book:
            self.books.remove(book)
            self.borrowed.append(book)
        else:
            print(f"Le livre {book_title} n'est pas dans la bibliothèque.")

    def return_book(self, book_title):
        book = self._find_book(book_title, self.borrowed)
        if book:
            self.books.append(book)
            self.borrowed.remove(book)
        else:
            print(f"Le livre {book_title} n'a pas été emprunté.")

    @staticmethod
    def _find_book(book_title, book_list):
        for book in book_list:
            if book.title == book_title:
                return book
        return None

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books(self):
        return [book.title for book in self.borrowed]


if __name__ == "__main__":
    lotr = Book("Le seigneur des anneaux", "J.R.R Tolkien", 1954)
    harry_potter = Book("Harry Potter", "J.K Rowling", 1997)

    lib = Library()
    lib.add_book(lotr)
    lib.add_book(harry_potter)
    print(lib.available_books())
    print(lib.borrowed_books())

    lib.remove_book("Le seigneur des anneaux")

    lib.borrow_book("Le seigneur des anneaux")
    print(lib.available_books())
    print(lib.borrowed_books())

    lib.return_book("Le seigneur des anneaux")
    print(lib.available_books())
    print(lib.borrowed_books())

