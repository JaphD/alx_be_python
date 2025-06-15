class Book():

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False  # already checked out

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False  # wasn't checked out
    
    def is_available(self):
        return not self.__is_checked_out
    
class Library():

    def __init__(self):
        self.__books = []

    def add_book(self, book: Book):
        self.__books.append(book)

    def check_out_book(self, title:str):
        for book in self.__books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"'{title}' is not available or doesn't exist.")

    def return_book(self, title:str):
        for book in self.__books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"'{title}' is not currently checked out or doesn't exist.")

    def list_available_books(self):
        available = False
        for book in self.__books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available = True
        if not available:
            print("No books available.")   