from dao.genres_dao import GenreDAO


class GenreService:

    def __init__(self, genre_dao: GenreDAO):
        self.dao = genre_dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)
