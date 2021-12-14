from entities.book import Book

from repositories.book_repository import book_repository
from repositories.course_repository import course_repository

class BookService:
    def __init__(self, repository=book_repository, course_repository=course_repository):
        self._repository = repository
        self._course_repository = course_repository

    def add_book(self, title, author, year, comment, course_name=None):
        print('service')
        course = course_repository.find_by_course_name(course_name)
        print('course', course)
        book = Book(title, author, year, comment)
        self._repository.add(book, course)

    def get_books(self):
        return self._repository.find_all()
    
    def get_book_by_id(self, id):
        return self._repository.find_by_id(id)

    def delete_book(self, id):
        self._repository.delete(id)
