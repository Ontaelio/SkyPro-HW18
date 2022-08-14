from flask_restx import Resource, Namespace

from container import genre_service
from dao.models.genres_model import GenreSchema

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:uid>/')
class GenreView(Resource):
    def get(self, uid):
        genre = genre_service.get_one(uid)
        return genre_schema.dump(genre), 200
