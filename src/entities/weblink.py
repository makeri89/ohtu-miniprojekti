from database import db
from entities.course_to_weblink import courses_to_weblinks

class Weblink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    comment = db.Column(db.String(500), nullable=False)
    courses = db.relationship(
        'Course',
        secondary=courses_to_weblinks,
        back_populates='weblinks'
    )

    def __init__(self, title=None, url=None, comment=None, course=None):
        self.title = title
        self.url = url
        self.comment = comment

    def __repr__(self):
        return f'{self.id}: {self.title} :: {self.url} :: {self.comment}'
