from database import db
from entities.course_to_podcast import courses_to_podcasts
from entities.course_to_book import courses_to_books
from entities.course_to_weblink import courses_to_weblinks

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    podcasts = db.relationship(
        'Podcast',
        secondary=courses_to_podcasts,
        back_populates='courses'
    )
    books = db.relationship(
        'Book',
        secondary=courses_to_books,
        back_populates='courses'
    )
    weblinks = db.relationship(
        'Weblink',
        secondary=courses_to_weblinks,
        back_populates='courses'
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.id}: {self.name}'
