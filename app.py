import requests
from flask import Flask, render_template, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from rq import Queue
from rq.job import Job
from worker import conn

app = Flask(__name__)
app.config["SECRET_KEY"] = "set-this-key"
app.config.from_object(Config)
db = SQLAlchemy(app)

# set up Redis connection nad initilized a queue based on that connection
q = Queue(connection=conn)

from models import Wordcount

def count_words(url):
	errors = []
	try:
		# print('>>>2')
		resp = requests.get(url)
		result = len(resp.text.split())
		# print('result:', result)
		# print('total number of urls', Wordcount.query.count())
		w = Wordcount(url=url, count=str(result))
		db.session.add(w)
		db.session.commit()
		return w.id
	except Exception as e:
		print('Error:', str(e))
		errors.append('Entered URL does not exist, try again!')
		# return {'error': errors}
		return render_template('index.html', errors=errors)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		# print('>>>1')
		url = request.form['url']
		if not url[:8].startswith(('https://', 'http"//')):
			url = 'http://' + url
		job = q.enqueue_call(func = count_words, args=(url,), result_ttl=5000)
		print(job.get_id())		
	return render_template('index.html', results=Wordcount.query.all())

# note-
# For the error - Error: (sqlite3.OperationalError) no such table:
# To create the initial database, just import the db object from an interactive Python shell and run the SQLAlchemy.create_all() method to create the tables and database:
# >>> from yourapplication import db
# >>> db.create_all()
# Ref - https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/