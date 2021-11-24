class Entity:
    def __init__(self, title: str):
        self.__title = title

    @property
    def get_title(self):
        return self.__title

class Weblink(Entity):
    def __init__(self, title: str, url: str):
        super().__init__(title)
        self.__url = url

    @property
    def get_url(self):
        return self.__url