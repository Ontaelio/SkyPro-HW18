# здесь контроллеры/хендлеры/представления для обработки запросов
# (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')

@movie_ns.route('/movies/')
class MoviesView(Resource):
    def get(self):
        return "got all", 200

    def post(self, data):
        return f"post a movie {data}", 201"

class MovieView(Resource):
    def get(self, uid):
        return f"got a movie #{uid}", 200

    def put(self, uid):
        return f"put a movie #{uid}", 200

#
#
# @book_ns.route('/')
# class BooksView(Resource):
#     def get(self):
#         return "", 200
#
#     def post(self):
#         return "", 201
