from entities.podcast import Podcast

from repositories.podcast_repository import podcast_repository

class PodcastService:
    def __init__(self, repository=podcast_repository):
        self._repository = repository

    def add_podcast(self, description, title, name):
        podcast = Podcast(description, title, name)
        self._repository.add(podcast)

    def get_podcasts(self):
        return self._repository.find_all()


