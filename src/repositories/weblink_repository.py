from src.database import db
from src.entities.weblink import Weblink

class WeblinkRepository:
    def __init__(self):
        pass

    def find_all(self):
        return Weblink.query.all()

    def add(self, weblink):
        db.session.add(weblink)
        db.session.commit()

weblink_repository = WeblinkRepository()
