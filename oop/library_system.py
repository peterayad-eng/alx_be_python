class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {book.title} by {book.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}"

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def list_books(self):
        for book in self.book_list:
            print (book)

