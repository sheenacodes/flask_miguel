from flask import render_template
from app import app
# import the app variable from the app package


@app.route('/')
@app.route('/index')
def index():
	user = {'username':'sheena'}
	return render_template('index.html',user=user)
