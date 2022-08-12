from flask_restx import Resource, Namespace

director_ns = Namespace('directors')

@director_ns.route('/directors/')
class directorsView(Resource):
    def get(self):
        return "got all", 200
    

@director_ns.route('/directors/<int:uid>')
class directorView(Resource):
    def get(self, uid):
        return f"got a dir #{uid}", 200