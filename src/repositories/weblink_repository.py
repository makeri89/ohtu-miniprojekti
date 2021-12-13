from database import db
from entities.weblink import Weblink

class WeblinkRepository:
    def __init__(self):
        pass

    def find_all(self):
        return Weblink.query.all()

    def add(self, weblink):
        db.session.add(weblink)
        db.session.commit()

    def delete(self, id):
        deleted_link = Weblink.query.get(id)
        db.session.delete(deleted_link)
        db.session.commit()

weblink_repository = WeblinkRepository()
