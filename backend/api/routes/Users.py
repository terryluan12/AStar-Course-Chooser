
from flask import jsonify
from flask_restx import Resource, reqparse
from api.models.mongoModel.User import User

# -------------------- User related --------------------
class UserRegistration(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        data = parser.parse_args()
        username = data['username']
        password = data['password']
        
        if User.objects(username=username):
            resp = jsonify({'message': 'Username already exists'})
            resp.status_code = 409
            return resp
        
        try:
            User.create(username, password)
            resp = jsonify({})
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp


class UserUpdatePwd(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        data = parser.parse_args()
        username = data['username']
        password = data['password']
        try:
            User.create(username, password)
            resp = jsonify({})
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp


class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        data = parser.parse_args()
        username = data['username']
        password = data['password']
        try:
            if User.verify_password(username, password):
                resp = jsonify({'username': username})
                resp.status_code = 200
            else:
                resp = jsonify({'message': 'Login failed'})
                resp.status_code = 401
                return resp
        except Exception as e:
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp
# ------------------------------------------------------------
