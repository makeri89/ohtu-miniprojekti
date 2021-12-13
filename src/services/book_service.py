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

    def delete_book(self, id):
        self._repository.delete(id)      
