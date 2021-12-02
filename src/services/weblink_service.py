from src.entities.weblink import Weblink

from src.repositories.weblink_repository import weblink_repository

class WeblinkService:
    def __init__(self, repository=weblink_repository):
        self._repository = repository

    def add_weblink(self, title, url):
        weblink = Weblink(title, url)
        self._repository.add(weblink)

    def get_weblinks(self):
        return self._repository.find_all()

    #placeholder before flask_testing is operational
    def create_weblink_for_testing(self, title, url):
        return Weblink(title, url)
