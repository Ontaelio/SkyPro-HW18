from flask_restx import Resource, Namespace

from dao.models.directors_model import DirectorSchema
from dao.directors_dao import DirectorDAO
from setup_db import db


director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)
director_dao = DirectorDAO(db.session)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_dao.get_all()
        return directors_schema.dump(all_directors), 200
    

@director_ns.route('/<int:uid>/')
class DirectorView(Resource):
    def get(self, uid):
        director = director_dao.get_one(uid)
        return director_schema.dump(director), 200
