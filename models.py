from app import db

class Wordcount(db.Model):
    __tablename__ = 'websites'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(120))
    count = db.Column(db.String(50))

def __init__(self, url, count):
        self.url = url
        self.count = count

def __repr__(self):
        return '<Wordcount {}>'.format(self.url)