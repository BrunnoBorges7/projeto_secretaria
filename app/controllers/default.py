from flask import render_template
from app import app

@app.route("/index/<user>")
@app.route("/", defaults={"user": None})
def index(user):
    return render_template('index', user=user)
