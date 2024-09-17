from flask import jsonify
from api.models.User import User
from flask_restx import Namespace, Resource, reqparse
from werkzeug.security import check_password_hash

api = Namespace('Session', description='Session/auth related operations')

@api.route('/session')
class SessionView(Resource):
    
    @api.doc(params={'username': 'User\'s username', 'password': 'User\'s password'})
    @api.doc(responses={200: 'User logged in', 401: 'Login failed', 404: 'Username Incorrect'})
    def post(self):
        resp = {}
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        data = parser.parse_args()
        attemptedPassword = data["password"]
        user = User.get(data["username"])
        
        if user is None:
            resp["message"] = "User " + data["username"] + " could not be found"
            return resp, 404
        
        if check_password_hash(user.password, attemptedPassword):
            resp["message"] = "User Logged In"
            return resp, 200
        else:
            resp["message"] = "Login failed"
            return resp, 401