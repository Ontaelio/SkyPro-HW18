from dao.directors_dao import DirectorDAO
from dao.genres_dao import GenreDAO
from dao.movies_dao import MovieDAO
from services.directors_service import DirectorService
from services.genres_service import GenreService
from services.movies_service import MovieService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)