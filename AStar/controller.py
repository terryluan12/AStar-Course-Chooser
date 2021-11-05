# this is the controller

from flask import jsonify, request
from flask_restful import Resource, reqparse
from config import app
from model import *

@app.route("/")
def app_connect():
    return "A-Star"

class UserRegistration(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        data = parser.parse_args()
        username = data['username']
        password = data['password']
        
        if User(username=username):
            resp = jsonify({'message': 'Username already exists'})
            resp.status_code = 409
            return resp
        
        try:
            User.create(username, password)
            resp.status_code = 200
            return resp
        except:
            resp.status_code = 400
            return resp


class ShowCourse(Resource):
    def get(self):
        code = request.args.get('code')
        if not Course(code=code):
            resp = jsonify({'message': f"Course {code} doesn't exist"})
            resp.status_code = 404
            return resp

        try:
            resp = jsonify({'course': Course.get(code)})
            resp.status_code = 200
            return resp
        except:
            resp.status_code = 400
            return resp
        