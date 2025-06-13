class Book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_availability(self):
        return self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_availability():
                    raise ValueError("The book is not available")
                else:
                    book._is_checked_out = True
                    break

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False
                break

    def list_available_books(self):
        for book in self._books:
            if not book.check_availability():
                print(f"{book.title} by {book.author}")
