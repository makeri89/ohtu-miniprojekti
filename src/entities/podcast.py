from database import db

class Podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self, title=None, name=None, description=None ):
        self.title = title
        self.name = name
        self.description = description

    def __repr__(self):
        return f'{self.id}: {self.title} :: {self.name} :: {self.description}'
