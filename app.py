# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

from flask import Flask
from flask_restx import Api

from config import Config
# from models import Review, Book
from setup_db import db
# from views.books import book_ns
# from views.reviews import review_ns
#
# функция создания основного объекта app
from views.movies_views import movie_ns
from views.genres_views import genre_ns
from views.directors_views import director_ns


def create_app(config_object):
    appl = Flask(__name__)
    appl.config.from_object(config_object)
    register_extensions(appl)
    return appl
#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(appl):
    db.init_app(appl)
    api = Api(appl)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    #create_data(app, db)


#
#
# функция
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#
#             db.session.add_all(здесь список созданных объектов)

config = Config()
app = create_app(config)
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
