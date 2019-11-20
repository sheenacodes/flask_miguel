from app import app
# import the app variable from the app package


@app.route('/')
@app.route('/index')
def index():
	return 'Hello, World!'
