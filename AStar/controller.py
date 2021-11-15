# this is the controller

from flask import jsonify, request
from flask_restful import Resource, reqparse
# from flask_cors import cross_origin
from config import app
from model import *
import sys

@app.route("/")
def app_connect():
    return "A-Star"

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
            resp = jsonify({'error': e})
            resp.status_code = 400
            return resp

    def get(self):
        code = request.args.get('code')

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
            resp = jsonify({'error': e})
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
            resp = jsonify({'error': e})
            resp.status_code = 400
            return resp
# ------------------------------------------------------------

# -------------------- Course related --------------------
class ShowCourse(Resource):
    def get(self):
        code = request.args.get('code')

        if not Course.objects(code=code):
            resp = jsonify({'message': f"Course {code} doesn't exist"})
            resp.status_code = 404
            return resp

        try:
            resp = jsonify({'course': Course.get(code)})
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({'error': e})
            resp.status_code = 400
            return resp

    
class SearchCourse(Resource):
    def get(self):
        input = request.args.get('input')
        resp = jsonify({'course_name': f"Software Engineering"})
        return resp

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('input', required=True)
        data = parser.parse_args()
        input = data['input']

# ------------------------------------------------------------

# -------------------- Wishlist related --------------------

class UserWishlist(Resource):
    def get(self):
        username = request.args.get('username')
        try:
            resp = jsonify({'wishlist': User.get_wishlist(username_=username)})
            resp.status_code = 200
            return resp
        except Exception as e: 
            resp = jsonify({'error': e})
            resp.status_code = 400
            return resp
    

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('wishlist', required=True)
        parser.add_argument('course', required=True)
        data = parser.parse_args()
        wishlist = data['wishlist']
        username = data['username']
        course = data['course']
        
        try:
            Wishlist.add_course(course) 
            resp = jsonify({'wishlist': wishlist})
            resp.status_code = 200
            return resp    
        except Exception as e:
            resp = jsonify({'error': e})
            resp.status_code = 400
            return resp


class UserWishlistAdd(Resource):
    def get(self):
        username = request.args.get('username')
        code = request.args.get('code')
        try:
            course = Course.get(code)
            wl = User.get_wishlist(username_=username)
            wl.add_course(course)
            resp = jsonify({'wishlist': wl})
            resp.status_code = 200
            return resp
        except Exception as e: 
            resp = jsonify({'error': e})
            resp.status_code = 400
            return resp

    # def post(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('username', required=True)
    #     parser.add_argument('wishlist', required=True)
    #     parser.add_argument('course', required=True)
    #     data = parser.parse_args()
    #     wishlist = data['wishlist']
    #     username = data['username']
    #     course = data['course']
        
    #     try:
    #         Wishlist.add_course(course) 
    #         resp = jsonify({'wishlist': wishlist})
    #         resp.status_code = 200
    #         return resp    
    #     except Exception as e:
    #         resp = jsonify({'error': e})
    #         resp.status_code = 400
    #         return resp


class UserWishlistRemove(Resource):
    def get(self):
        username = request.args.get('username')
        code = request.args.get('code')
        try:
            course = Course.get(code)
            wl = User.get_wishlist(username_=username)
            wl.remove_course(course)
            resp = jsonify({'wishlist': wl})
            resp.status_code = 200
            return resp
        except Exception as e: 
            resp = jsonify({'error': e})
            resp.status_code = 400
            return resp
    

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('wishlist', required=True)
        parser.add_argument('course', required=True)
        data = parser.parse_args()
        wishlist = data['wishlist']
        username = data['username']
        course = data['course']
        
        try:
            Wishlist.add_course(course) 
            resp = jsonify({'wishlist': wishlist})
            resp.status_code = 200
            return resp    
        except Exception as e:
            resp = jsonify({'error': e})
            resp.status_code = 400
            return resp


class UserWishlistMinorCheck(Resource):
    def get(self):
        username = request.args.get('username')

        try:
            wl = User.get_wishlist(username_=username)
            courses = [c.code for c in wl.course]
            print(courses)
            check = Minor.check(codes_=courses)
            print(check)
            resp = jsonify({'minorCheck': check})
            resp.status_code = 200
            return resp
        except Exception as e: 
            resp = jsonify({'error': e})
            resp.status_code = 400
            return resp
    

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('wishlist', required=True)
        parser.add_argument('course', required=True)
        data = parser.parse_args()
        wishlist = data['wishlist']
        username = data['username']
        course = data['course']
        
        try:
            Wishlist.add_course(course) 
            resp = jsonify({'wishlist': wishlist})
            resp.status_code = 200
            return resp    
        except Exception as e:
            resp = jsonify({'error': e})
            resp.status_code = 400
            return resp
            