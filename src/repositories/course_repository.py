from database import db
from entities.course import Course

class CourseRepository:
    def __init__(self):
        pass

    def find_all(self):
        return Course.query.all()

    def find_by_id(self, course_id):
        return Course.query.get(course_id)

    def find_by_course_name(self, course_name):
        return Course.query.filter_by(name=course_name).first()

    def add(self, course):
        db.session.add(course)
        db.session.commit()

    def delete(self, course_id):
        deleted_course = Course.query.get(course_id)
        db.session.delete(deleted_course)
        db.session.commit()

course_repository = CourseRepository()
