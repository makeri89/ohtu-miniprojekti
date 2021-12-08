from database import db
from entities.podcast import Podcast

class PodcastRepository:
    def __init__(self):
        pass

    def find_all(self):
        return Podcast.query.all()

    def add(self, podcast):
        db.session.add(podcast)
        db.session.commit()

podcast_repository = PodcastRepository()
