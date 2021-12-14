from database import db

courses_to_podcasts = db.Table('courses_to_podcasts',
    db.Column('course_id', db.Integer,
              db.ForeignKey('course.id'), primary_key=True),
    db.Column('podcast_id', db.Integer,
              db.ForeignKey('podcast.id'), primary_key=True),
)
