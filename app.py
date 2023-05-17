import os
from flask import Flask, redirect
from routes.players_routes import players_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes

SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "ghjdfghdg")



app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


app.register_blueprint(players_routes, url_prefix='/players')
app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')


@app.route('/')
def index():
  return redirect('/players')