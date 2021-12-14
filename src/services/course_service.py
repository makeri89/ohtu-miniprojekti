from entities.course import Course
from repositories.course_repository import course_repository

class CourseService:
    def __init__(self, repository=course_repository):
        self._repository = repository

    def get_courses(self):
        return self._repository.find_all()

    def get_course_by_id(self, course_id):
        return self._repository.find_by_id(course_id)

    def add_course(self, name):
        course = Course(name)
        self._repository.add(course)

    def delete_course(self, course_id):
        self._repository.delete(course_id)
