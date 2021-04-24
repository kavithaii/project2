from app import db

class Websites(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String(120))
	count = db.Column(db.String(50))

	def __repr__(self):
		return '<Websites {}>'.format(self.url)