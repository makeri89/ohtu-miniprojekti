from database import db
from entities.podcast import Podcast

class PodcastRepository:
    def __init__(self):
        pass

    def find_all(self):
        return Podcast.query.all()

    def find_by_id(self, podcast_id):
        return Podcast.query.get(podcast_id)

    def add(self, podcast, course):
        podcast.courses.append(course)
        db.session.add(podcast)
        db.session.commit()

    def delete(self, podcast_id):
        deleted_podcast = Podcast.query.get(podcast_id)
        db.session.delete(deleted_podcast)
        db.session.commit()

podcast_repository = PodcastRepository()
