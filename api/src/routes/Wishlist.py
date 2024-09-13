from flask import jsonify, request
from flask_restful import Resource, reqparse
from src.models.mongoModel.User import User
from src.models.mongoModel.Minor import Minor
from src.models.sqlModel.Course import Course

# -------------------- Wishlist related --------------------
class UserWishlist(Resource):
    def get(self):
        username = request.args.get('username')
        try:
            resp = jsonify({'wishlist': User.get_wishlist(username_=username).expand()})
            resp.status_code = 200
            return resp
        except Exception as e: 
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        data = parser.parse_args()
        username = data['username']
        try:
            resp = jsonify({'wishlist': User.get_wishlist(username_=username).expand()})
            resp.status_code = 200
            return resp
        except Exception as e: 
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('code', required=True)
        data = parser.parse_args()
        code = data['code']
        if not Course.objects(code=code):
            resp = jsonify({'message': f"Course {code} doesn't exist"})
            resp.status_code = 404
            return resp        
# ------------------------------------------------------------

class UserWishlistAdd(Resource):
    def get(self):
        username = request.args.get('username')
        code = request.args.get('code')
        try:
            course = Course.get(code)
            wl = User.get_wishlist(username_=username)
            wl.add_course(course)
            resp = jsonify({'wishlist': wl.expand()})
            resp.status_code = 200
            return resp
        except Exception as e: 
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('code', required=True)
        data = parser.parse_args()
        username = data['username']
        code = data['code']
        try:
            course = Course.get(code)
            wl = User.get_wishlist(username_=username)
            wl.add_course(course)
            resp = jsonify({'wishlist': wl.expand()})
            resp.status_code = 200
            return resp
        except Exception as e: 
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp


class UserWishlistRemove(Resource):
    def get(self):
        username = request.args.get('username')
        code = request.args.get('code')
        try:
            course = Course.get(code)
            wl = User.get_wishlist(username_=username)
            wl.remove_course(course)
            resp = jsonify({'wishlist': wl.expand()})
            resp.status_code = 200
            return resp
        except Exception as e: 
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('code', required=True)
        data = parser.parse_args()
        username = data['username']
        code = data['code']
        try:
            course = Course.get(code)
            wl = User.get_wishlist(username_=username)
            wl.remove_course(course)
            resp = jsonify({'wishlist': wl.expand()})
            resp.status_code = 200
            return resp
        except Exception as e: 
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp


class UserWishlistMinorCheck(Resource):
    def get(self):
        username = request.args.get('username')
        try:
            wl = User.get_wishlist(username_=username)
            courses = [c.code for c in wl.course]
            check = Minor.check(codes_=courses)
            resp = jsonify({'minorCheck': check})
            resp.status_code = 200
            return resp
        except Exception as e: 
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        data = parser.parse_args()
        username = data['username']
        try:
            wl = User.get_wishlist(username_=username)
            courses = [c.code for c in wl.course]
            check = Minor.check(codes_=courses)
            resp = jsonify({'minorCheck': check})
            resp.status_code = 200
            return resp
        except Exception as e: 
            resp = jsonify({'error': 'something went wrong'})
            resp.status_code = 400
            return resp
            
