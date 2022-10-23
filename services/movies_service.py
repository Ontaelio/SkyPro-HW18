
from dao.movies_dao import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.dao = movie_dao

    def get_all(self, args):
        if 'director_id' in args:
            return self.dao.get_by_director(args['director_id'])
        if 'genre_id' in args:
            return self.dao.get_by_genre(args['genre_id'])
        if 'year' in args:
            return self.dao.get_by_year(args['year'])
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def add_one(self, data):
        self.dao.add_one(data)

    def update(self, uid, data):
        movie = self.get_one(uid)
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        self.dao.update(movie)

    def delete(self, uid):
        self.dao.delete(uid)

    def get_by_director(self, did):
        self.dao.get_by_director(did)

    def get_by_genre(self, gid):
        self.dao.get_by_genre(gid)

    def get_by_year(self, year):
        self.dao.get_by_year(year)



