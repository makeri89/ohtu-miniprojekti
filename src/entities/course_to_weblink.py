from database import db

courses_to_weblinks = db.Table('courses_to_weblinks',
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True),
    db.Column('weblink_id', db.Integer, db.ForeignKey('weblink.id'), primary_key=True),
)
