from database import db
from entities.course_to_podcast import courses_to_podcasts

class Podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    comment = db.Column(db.String(500), nullable=False)
    courses = db.relationship(
        'Course',
        secondary=courses_to_podcasts,
        back_populates='podcasts'
    )

    def __init__(self, title=None, name=None,
                 description=None, comment=None,
                 course=None):
        self.title = title
        self.name = name
        self.description = description
        self.comment = comment
        self.courses = []

    def __repr__(self):
        return f'{self.id}: {self.title} :: {self.name} :: \
            {self.description} :: {self.comment}'
