from flask import Flask, g
import models

DEBUG = True
PORT = 8000
HOST = "0.0.0.0"

app = Flask(__name__)
app.secret_key = "slljfweisdfjskbqwbasndmfniewhfh2r34hrew89yfheuwbsd"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(userid):
	try:
		return models.User.get(models.User.id == userid)
	except models.DoesNotExist:
		return None

@app.before_request
def before_request():
	# Connect to DB before each before_request
	g.db = models.DATABASE
	g.db.connect()


@app.after_request
def after_request(response):
	# Close DB connection after each after_request
	g.db.close()
	return response







if __name__ == "__main__":
	models.initialize()
	models.User.create_user(
		name="rohanadmin",
		email="rohankagrawal@gmail.com",
		password="")
	app.run(debug=DEBUG, host=HOST, port=PORT)