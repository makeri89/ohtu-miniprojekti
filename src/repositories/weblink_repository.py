from database import db
from entities.weblink import Weblink

class WeblinkRepository:
    def __init__(self):
        pass

    def find_all(self):
        return Weblink.query.all()

    def find_by_id(self, weblink_id):
        return Weblink.query.get(weblink_id)

    def add(self, weblink, course):
        weblink.courses.append(course)
        db.session.add(weblink)
        db.session.commit()

    def delete(self, weblink_id):
        deleted_link = Weblink.query.get(weblink_id)
        db.session.delete(deleted_link)
        db.session.commit()

weblink_repository = WeblinkRepository()
