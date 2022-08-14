from dao.directors_dao import DirectorDAO


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.dao = director_dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)
