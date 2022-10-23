from dao.models.directors_model import Director


class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, uid):
        return self.session.query(Director).get(uid)
