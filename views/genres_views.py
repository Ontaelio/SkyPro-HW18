from flask_restx import Resource, Namespace

from dao.models.genres_model import GenreSchema
from dao.genres_dao import GenreDAO
from setup_db import db

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
genre_dao = GenreDAO(db.session)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_dao.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:uid>/')
class GenreView(Resource):
    def get(self, uid):
        genre = genre_dao.get_one(uid)
        return genre_schema.dump(genre), 200
