# здесь контроллеры/хендлеры/представления для обработки запросов
# (flask ручки). сюда импортируются сервисы из пакета services

from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')

@movie_ns.route('/movies/')
class MoviesView(Resource):
    def get(self):
        return "got all", 200

    def post(self):
        return f"post a movie", 201

@movie_ns.route('/movies/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        return f"got a movie #{uid}", 200

    def put(self, uid):
        return f"put a movie #{uid}", 200

    def delete(self, uid):
        return f"No more movie #{uid}", 204


