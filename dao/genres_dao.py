from dao.models.genres_model import Genre


class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, uid):
        return self.session.query(Genre).get(uid)
