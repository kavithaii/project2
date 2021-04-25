import requests
from flask import Flask, render_template, request
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "set-this-key"
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import Wordcount

@app.route('/', methods=['GET', 'POST'])
def index():
	errors = []
	if request.method == 'POST':
		print('>>>1')
		try:
			print('>>>2')
			url = request.form['url']
			resp = requests.get(url)
			result = len(resp.text.split())
			print('result:', result)
			print('total number of urls', Wordcount.query.count())
			w = Wordcount(url=url, count=str(result))
			db.session.add(w)
			db.session.commit()
		except Exception as e:
			print('Error:', str(e))
			errors.append('Entered URL does not exist, try again!')
	return render_template('index.html', errors=errors)