# здесь контроллеры/хендлеры/представления для обработки запросов
# (flask ручки). сюда импортируются сервисы из пакета services
from flask import request
from flask_restx import Resource, Namespace

from dao.models.movies_model import MovieSchema
from dao.movies_dao import MovieDAO

from dao.models.directors_model import DirectorSchema
from dao.models.genres_model import GenreSchema
from setup_db import db

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
movie_dao = MovieDAO(db.session)

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = movie_dao.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        movie_json = request.json
        movie_dao.add_one(movie_json)
        return "", 201


@movie_ns.route('/<int:uid>/')
class MovieView(Resource):
    def get(self, uid):
        movie = movie_dao.get_one(uid)
        return movie_schema.dump(movie), 200

    def put(self, uid):
        data = request.json
        movie_dao.update(uid, data)
        return "", 204

    def delete(self, uid):
        movie_dao.delete(uid)
        return "", 204


@movie_ns.route('/director/<int:did>/')
class MoviesByDirectorView(Resource):
    
    def get(self, did):
        movies = movie_dao.get_by_director(did)
        return movies_schema.dump(movies), 200


@movie_ns.route('/genre/<int:gid>/')
class MoviesByGenreView(Resource):

    def get(self, gid):
        movies = movie_dao.get_by_genre(gid)
        return movies_schema.dump(movies), 200
    
@movie_ns.route('/year/<int:year>/')
class MoviesByYearView(Resource):

    def get(self, year):
        movies = movie_dao.get_by_year(year)
        return movies_schema.dump(movies), 200

