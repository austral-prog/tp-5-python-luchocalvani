from src.Book import Book
from src.User import User


class Library:
    def __init__(self):
        self.__books: list[Book] = []
        self.__users: list[User] = []
        self.__checked_out_books: list[list[str]] = []
        self.__checked_in_books: list[list[str]] = []

    # Getters
    def get_books(self) -> list[Book]:
        return self.__books

    def get_users(self) -> list[User]:
        return self.__users

    def get_checked_out_books(self) -> list[list[str]]:
        return self.__checked_out_books

    def get_checked_in_books(self) -> list[list[str]]:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn: str, title: str, author: str) -> None:
        libro = Book(isbn, title, author)
        for book in self.__books:
            if book.get_isbn() == isbn:
                return None
        self.__books.append(libro)

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books:
            print(f"ISBN: {book.get_isbn()}, Title: {book.get_title()}, Author: {book.get_author()}")

    # 2.1 Check out book
    def check_out_book(self, isbn: str, dni: str, due_date: str) -> str:
        verif1: bool = False
        verif2: bool = False
        for user in self.__users:
            if user.get_dni() == dni:
                verif1 = True
        for book in self.__books:
            if book.get_isbn() == isbn:
                verif2 = True
                if book.is_available():
                    self.__checked_out_books.append([isbn, dni, due_date])
                    book.set_available(False)
                    book.increment_checkout_num()
                    user.increment_checkouts()
                    return f"User {user} checked out book {isbn}"
                else:
                    return f"Book {isbn} is not available"
        if verif1 == False or verif2 == False:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

    # 2.2 Check in book
    def check_in_book(self, isbn: str, dni: str, returned_date: str) -> str:
        for book in self.__books:
            if book.get_isbn() == isbn:
                if not book.is_available():
                    book.set_available(True)
                    self.__checked_in_books.append([isbn, dni, returned_date])
                    return f"Book {isbn} checked in by user {dni}"
                else:
                    return f"Book {isbn} is not available"
        return f"Book {isbn} is not available"


    # Utils
    def add_user(self, dni, name) -> None:
        new_user = User(dni, name)
        for user in self.__users:
            if user.get_dni() == dni:
                return None
        self.__users.append(new_user)
