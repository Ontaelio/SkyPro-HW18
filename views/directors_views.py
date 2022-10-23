from flask_restx import Resource, Namespace

from container import director_service
from dao.models.directors_model import DirectorSchema

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200
    

@director_ns.route('/<int:uid>/')
class DirectorView(Resource):
    def get(self, uid):
        director = director_service.get_one(uid)
        return director_schema.dump(director), 200
