from flask import jsonify
from flask_restx import Namespace, Resource, reqparse
from api.models.User import User
from werkzeug.security import generate_password_hash, check_password_hash

api = Namespace('Users', description='User related operations')

@api.route('/user')
class UserView(Resource):
    #TODO Remove deprecated reqparse
    @api.doc(params={'username': 'User\'s username', 'password': 'User\'s password'})
    @api.doc(responses={ 201: 'User created', 409: 'Username already exists'})
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        data = parser.parse_args()
        username = data["username"]
        password = generate_password_hash(data["password"])

        if User.get(username):
            resp = jsonify({"message": "Username already exists"})
            resp.status_code = 409
            return resp

        try:
            User.create(username, password)
            resp = jsonify({})
            resp.status_code = 201
            return resp
        except Exception as e:
            resp = jsonify({"error": e})
            resp.status_code = 400
            return resp
    
    @api.doc(params={'username': 'User\'s username', 'password': 'User\'s password'})
    @api.doc(responses={200: 'Success - Password changed', 404: 'User not found'})
    def patch(self):
        # TODO FIX PASSWORD UPDATE
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        data = parser.parse_args()
        username = data["username"]
        password = data["password"]
        try:
            User.update(username, generate_password_hash(password))
            resp = jsonify({})
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({"error": "something went wrong"})
            resp.status_code = 400
            return resp

    @api.doc(params={'username': 'User\'s username '})
    @api.doc(responses={200: 'Success - User deleted', 404: 'User not found'})
    def delete(self):
        # TODO add verification
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        data = parser.parse_args()
        user = User.get(data["username"])
        attemptedPassword = data["password"]
        try:
            if check_password_hash(user.password, attemptedPassword):
                User.delete(data["username"], user.password)
                resp = jsonify({})
                resp.status_code = 200
                return resp
        except Exception as e:
            resp = jsonify({"error": "something went wrong"})
            resp.status_code = 400
            return resp

