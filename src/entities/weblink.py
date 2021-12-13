from database import db

class Weblink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    comment = db.Column(db.String(500), nullable=False)

    def __init__(self, title=None, url=None, comment=None):
        self.title = title
        self.url = url
        self.comment = comment

    def __repr__(self):
        return f'{self.id}: {self.title} :: {self.url} :: {self.comment}'
