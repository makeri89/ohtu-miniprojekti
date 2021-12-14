from database import db
from entities.course import Course

class CourseRepository:
    def __init__(self):
        pass
    
    def find_all(self):
        return Course.query.all()
    
    def add(self, course):
        db.session.add(course)
        db.session.commit()
        
    def delete(self, id):
        deleted_course = Course.query.get(id)
        db.session.delete(deleted_course)
        db.session.commit()
    
course_repository = CourseRepository()
