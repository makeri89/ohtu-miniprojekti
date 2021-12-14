from database import db
from entities.book import Book

class BookRepository:
    def __init__(self):
        pass

    def find_all(self):
        return Book.query.all()

    def find_by_id(self, book_id):
        return Book.query.get(book_id)

    def add(self, book, course):
        book.courses.append(course)
        db.session.add(book)
        db.session.commit()

    def delete(self, book_id):
        deleted_book = Book.query.get(book_id)
        db.session.delete(deleted_book)
        db.session.commit()

book_repository = BookRepository()
