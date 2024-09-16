from flask import jsonify
from flask_restx import reqparse
from api.models.sqlModel.User import User
from flask_restx import Namespace, Resource, reqparse
from werkzeug.security import check_password_hash

api = Namespace('Session', description='Session/auth related operations')

@api.route('/session')
class SessionView(Resource):
    
    @api.doc(params={'username': 'User\'s username', 'username': 'User\'s password'})
    @api.doc(responses={200: 'User logged in', 401: 'Login failed'})
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        data = parser.parse_args()
        attemptedPassword = data["password"]
        user = User.get(data["username"])
        try:
            if check_password_hash(user.password, attemptedPassword):
                resp = jsonify({"username": user["username"]})
                resp.status_code = 200
            else:
                resp = jsonify({"message": "Login failed"})
                resp.status_code = 401
                return resp
        except Exception as e:
            resp = jsonify({"error": e})
            resp.status_code = 400
            return resp
