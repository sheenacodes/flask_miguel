from flask import render_template
from app import app
# import the app variable from the app package


@app.route('/')
@app.route('/index')
def index():
	user = {'username':'sheena'}
	posts = [
		{
		'author':{'username':'John'},
		'body':'Beatiful day in Espoo'
		},
		{
		'author': {'username':'Susan'},
		'body':'The Avengers movies was cool'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)
