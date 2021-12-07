from database import db

class Podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    title = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(500), nullable=False)

    def __init__(self, description=None, title=None, name=None):
        self.description = description 
        self.title = title 
        self.name = name

    def __repr__(self):
        return f'{self.id}: {self.description} :: {self.title} :: {self.name}'
