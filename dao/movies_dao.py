from dao.models.movies_model import Movie

#crud
class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, uid):
        return self.session.query(Movie).get(uid)

    def add_one(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return 1

    def update(self, uid, data):
        movie = self.session.query(Movie).get(uid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        self.session.add(movie)
        self.session.commit()

        return 1

    def delete(self, uid):
        movie = self.session.query(Movie).get(uid)
        self.session.delete(movie)
        self.session.commit()
        return 1

    def get_by_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()




if __name__ == '__main__':
    a = MovieDAO()
    print (a.get_all())



# class BookDAO:
#     def get_all_books(self):
#         books = Book.query.all()
#         return