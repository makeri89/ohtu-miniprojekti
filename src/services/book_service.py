from entities.book import Book

from repositories.book_repository import book_repository

class BookService:
    def __init__(self, repository=book_repository):
        self._repository = repository

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self._repository.add(book)

    def get_books(self):
        return self._repository.find_all()

    #placeholder before flask_testing is operational
    def create_book_for_testing(self, title, author, year):
        return Book(title, author, year)
