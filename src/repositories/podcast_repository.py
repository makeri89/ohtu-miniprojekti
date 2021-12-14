from database import db
from entities.podcast import Podcast

class PodcastRepository:
    def __init__(self):
        pass

    def find_all(self):
        return Podcast.query.all()
    
    def find_by_id(self, id):
        return Podcast.query.get(id)

    def add(self, podcast, course):
        podcast.courses.append(course)
        db.session.add(podcast)
        db.session.commit()

    def delete(self, id):
        deleted_podcast = Podcast.query.get(id)
        db.session.delete(deleted_podcast)
        db.session.commit()

podcast_repository = PodcastRepository()
