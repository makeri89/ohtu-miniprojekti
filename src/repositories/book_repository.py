from database import db
from entities.book import Book

class BookRepository:
    def __init__(self):
        pass

    def find_all(self):
        return Book.query.all()

    def add(self, book):
        db.session.add(book)
        db.session.commit()

book_repository = BookRepository()