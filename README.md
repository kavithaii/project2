# Challenge
The goal is to implement a job queue feature in a flask web app backed by a database.
  
There is only one type of job to be queued, => counting the words in the webpage returned by user-submitted url.
  
(sample function definition in tasks.py)
```  
import requests
def count_words_at_url(url):
resp = requests.get(url)
return len(resp.text.split())
```
This job should be queued up asynchronously, and the results should be saved in the database.
  
The results should be displayed on the index page when the user navigates to it.
  
The user of this web app should be able to:
- navigate to the index page served by this flask application 
- submit a url 
- see results of submitted jobs
  
###### Suggested packages: 
- flask 
- flask-rq (or simple rq) 
- sqlalchemy - redis

## Instructions: to start this web app

- Create virtual environment 
      
      ```   $ virtualenv venv
            $ source venv/bin/activate
      ```
- Install necessary libraries from **requirements.txt**

       ```$ pip install -r requirements.txt```
- Start the develoment server
  
      ```$flask run```
- Browse to http://localhost:5000
- You can enter url, same page displays the list of URLs and their word count

##### Refernces:
[blog.miguelgrinberg.com](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)

[flask.palletsprojects.com - sqlite](https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/)

[realpython.com - Redis](https://realpython.com/flask-by-example-implementing-a-redis-task-queue/)

[pythonprogramming.net - Error handling](https://pythonprogramming.net/flask-error-handling-basics/)

[Python sqlite3.OperationalError: no such table:](https://stackoverflow.com/questions/28126140/python-sqlite3-operationalerror-no-such-table)

[jonathansoma.com](http://jonathansoma.com/tutorials/flask-sqlalchemy-mapbox/connecting-flask-to-sqlite.html)

[sqlite quick start](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)

[pythonbasics.org](https://pythonbasics.org/flask-sqlalchemy/)

[python-adv-web-apps.readthedocs.io](https://python-adv-web-apps.readthedocs.io/en/latest/flask_db1.html)

[www.pythonanywhere.com](https://www.pythonanywhere.com/forums/)
