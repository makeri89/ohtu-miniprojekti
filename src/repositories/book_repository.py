from database import db
from entities.book import Book

class BookRepository:
    def __init__(self):
        pass

    def find_all(self):
        return Book.query.all()
    
    def find_by_id(self, id):
        return Book.query.get(id)

    def add(self, book, course):
        book.courses.append(course)
        db.session.add(book)
        db.session.commit()

    def delete(self, id):
        deleted_book = Book.query.get(id)
        db.session.delete(deleted_book)
        db.session.commit()

book_repository = BookRepository()
