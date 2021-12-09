from database import db
from entities.weblink import Weblink
from routes import weblinks

class WeblinkRepository:
    def __init__(self):
        pass

    def find_all(self):
        return Weblink.query.all()

    def add(self, weblink):
        db.session.add(weblink)
        db.session.commit()

    def delete(self, id):
        db.session.query(Weblink).filter(Weblink.id==id).delete()
        db.session.commit()    

weblink_repository = WeblinkRepository()
