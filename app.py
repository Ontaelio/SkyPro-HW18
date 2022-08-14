from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db

from views.movies_views import movie_ns
from views.genres_views import genre_ns
from views.directors_views import director_ns


def create_app(config_object):
    appl = Flask(__name__)
    appl.config.from_object(config_object)
    register_extensions(appl)
    return appl


def register_extensions(appl):
    db.init_app(appl)
    api = Api(appl)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    # create_data(app, db)


config = Config()
app = create_app(config)
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
