from entities.podcast import Podcast

from repositories.podcast_repository import podcast_repository

class PodcastService:
    def __init__(self, repository=podcast_repository):
        self._repository = repository

    def add_podcast(self, title, name, description):
        podcast = Podcast(title, name, description)
        self._repository.add(podcast)

    def get_podcasts(self):
        return self._repository.find_all()

    def delete_podcast(self, id):
        self._repository.delete(id)