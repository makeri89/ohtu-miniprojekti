from database import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=True)
    comment = db.Column(db.String(500), nullable=False)

    def __init__(self, title=None, author=None, year=None, comment=None):
        self.title = title
        self.author = author
        self.year = year
        self.comment = comment

    def __repr__(self):
        return f'{self.id}: {self.author} :: {self.title} :: {self.year} :: {self.comment}'
