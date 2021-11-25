#temporary: move to proper modules!
from app import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
#temporary: ends

class Weblink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'{self.id}: {self.title} :: {self.url}'