from flask import request
from flask_restx import Resource, Namespace

from dao.models.movies_model import MovieSchema
from container import movie_service, movie_dao

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        args = request.args
        all_movies = movie_service.get_all(args)
        return movies_schema.dump(all_movies), 200

    def post(self):
        movie_json = request.json
        movie_service.add_one(movie_json)
        return "", 201


@movie_ns.route('/<int:uid>/')
class MovieView(Resource):
    def get(self, uid):
        movie = movie_service.get_one(uid)
        return movie_schema.dump(movie), 200

    def put(self, uid):
        data = request.json
        movie_service.update(uid, data)
        return "", 204

    def delete(self, uid):
        movie_service.delete(uid)
        return "", 204

# The following are deprecated, kept for possible backwards compatibility


@movie_ns.route('/director/<int:did>/')
class MoviesByDirectorView(Resource):
    
    def get(self, did):
        movies = movie_service.get_by_director(did)
        return movies_schema.dump(movies), 200


@movie_ns.route('/genre/<int:gid>/')
class MoviesByGenreView(Resource):

    def get(self, gid):
        movies = movie_service.get_by_genre(gid)
        return movies_schema.dump(movies), 200
    
@movie_ns.route('/year/<int:year>/')
class MoviesByYearView(Resource):

    def get(self, year):
        movies = movie_service.get_by_year(year)
        return movies_schema.dump(movies), 200


