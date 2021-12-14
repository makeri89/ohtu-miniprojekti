from entities.weblink import Weblink

from repositories.weblink_repository import weblink_repository
from repositories.course_repository import course_repository

class WeblinkService:
    def __init__(self, repository=weblink_repository):
        self._repository = repository

    def add_weblink(self, title, url, comment, course_name=None):
        course = course_repository.find_by_course_name(course_name)
        weblink = Weblink(title, url, comment)
        self._repository.add(weblink, course)

    def get_weblinks(self):
        return self._repository.find_all()

    def get_weblink_by_id(self, weblink_id):
        return self._repository.find_by_id(weblink_id)

    def delete_weblink(self, weblink_id):
        self._repository.delete(weblink_id)
