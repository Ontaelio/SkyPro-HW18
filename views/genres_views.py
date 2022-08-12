from flask_restx import Resource, Namespace

genre_ns = Namespace('genres')

@genre_ns.route('/genres/')
class genresView(Resource):
    def get(self):
        return "got all", 200
    
@genre_ns.route('/genres/<int:uid>')
class genreView(Resource):
    def get(self, uid):
        return f"got a genre #{uid}", 200