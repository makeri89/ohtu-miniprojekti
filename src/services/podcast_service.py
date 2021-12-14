from entities.podcast import Podcast

from repositories.podcast_repository import podcast_repository
from repositories.course_repository import course_repository

class PodcastService:
    def __init__(self, repository=podcast_repository,
                 c_repository=course_repository):
        self._repository = repository
        self._course_repository = c_repository

    def add_podcast(self, title, name, description, comment, course_name=None):
        course = self._course_repository.find_by_course_name(course_name)
        podcast = Podcast(title, name, description, comment)
        self._repository.add(podcast, course)

    def get_podcasts(self):
        return self._repository.find_all()

    def get_podcast_by_id(self, podcast_id):
        return self._repository.find_by_id(podcast_id)

    def delete_podcast(self, podcast_id):
        self._repository.delete(podcast_id)
