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
            User.put(username, password)
            resp = jsonify({})
            resp.status_code = 201
            return resp
        except Exception as e:
            resp = jsonify({"error": e})
            resp.status_code = 400
            return resp
    
    @api.doc(params={'username': 'User\'s username', 'oldPassword': 'Password to change from', 'newPassword': 'Password to change to'})
    @api.doc(responses={200: 'Success - Password changed', 404: 'User not found'})
    def patch(self):
        # TODO FIX PASSWORD UPDATE
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("oldPassword", required=True)
        parser.add_argument("newPassword", required=True)
        data = parser.parse_args()
        username = data["username"]
        password = data["oldPassword"]
        try:
            User.update(username, generate_password_hash(password))
            resp = jsonify({})
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({"error": "something went wrong"})
            resp.status_code = 400
            return resp

    @api.doc(params={'username': 'User\'s username ', 'password': 'User\'s password'})
    @api.doc(responses={200: 'Success - User deleted', 404: 'User not found', 404: 'Something went wrong'})
    def delete(self):
        resp = jsonify()
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        data = parser.parse_args()
        user = User.get(data["username"])
        attemptedPassword = data["password"]
        
        if user is None:
            resp.status = "error"
            resp.status_code = 404
            resp.message = "User " + data["username"] + " could not be found"

        try:
            if check_password_hash(user.password, attemptedPassword):
                User.delete(data["username"], user.password)
                resp.status = "success"
                resp.status_code = 200
                resp.message = "User " + data["username"] + " deleted"
                return resp
            else:
                resp.status = "error"
                resp.status_code = 401
                resp.message = "Password Incorrect"
                return resp
        except Exception as e:
            resp.status = "error"
            resp.status_code = 400
            resp.message = "something went wrong\n" + str(e)
            return resp

