from entities.weblink import Weblink

from repositories.weblink_repository import weblink_repository

class WeblinkService:
    def __init__(self, repository=weblink_repository):
        self._repository = repository

    def add_weblink(self, title, url):
        weblink = Weblink(title, url)
        self._repository.add(weblink)

    def get_weblinks(self):
        return self._repository.find_all()

    def delete_weblink(self, id):
        self._repository.delete(id)
