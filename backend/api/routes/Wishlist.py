from flask import jsonify, request
from flask_restx import Namespace, Resource, reqparse
from api.models.User import User
from api.models.Course import Course


api = Namespace('Wishlists', description='Wishlist related operations')


@api.route('/wishlist')
class WishlistView(Resource):

    @api.doc(params={'username': 'User\'s username'})
    @api.doc(responses={200: 'Wishlist Items retrieved', 404: 'User not found'})
    def get(self):
        resp = {}
        username = request.args.get("username")
        user = User.get(username)
        
        if user is None:
            resp["message"] = "User " + username + " could not be found"
            return resp, 404
        else:
            wishlistItems = user.getWishlist()
            resp["message"] = "Wishlist Items retrieved"
            resp["wishlist"] = [wishlistItem.to_json() for wishlistItem in wishlistItems]
            return resp, 200

    @api.doc(params={'username': 'User\'s username', 'course_code': 'Course Code'})
    @api.doc(responses={ 200: 'Course added to wishlist', 400: 'Course already in Wishlist', 404: 'User or Course not found'})
    def post(self):
        resp = {}
        username = request.args.get("username")
        code = request.args.get("course_code")
        # try:
        user = User.get(username)
        courses = Course.get(code)
        
        if user is None:
            resp["message"] = "User " + username + " could not be found"
            return resp, 404
        elif not courses or len(courses) != 1:
            resp["message"] = "Course " + code + " not found"
            return resp, 404
        
        if user.appendWishlist(courses[0]):
            resp["message"] = "Course added to wishlist"
            return resp, 200
        else:
            resp["message"] = "Course " + code + " already in Wishlist"
            return resp, 400

    @api.doc(params={'username': 'User\'s username', 'code': 'Course Code'})
    @api.doc(responses={ 200: 'Wishlist Item deleted', 400: 'Course not in Wishlist', 404: 'User or Course not found'})
    def delete(self):
        resp = {}
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("code", required=True)
        data = parser.parse_args()
        username = data["username"]
        code = data["code"]
        user = User.get(username)
        courses = Course.get(code)
            
        if user is None:
            resp["message"] = "User " + username + " could not be found"
            return resp, 404
        elif not courses or len(courses) != 1:
            resp["message"] = "Course " + code + " not found"
            return resp, 404
        
        if user.removeWishlist(courses[0]):
            resp["message"] = "Removed course"
            return resp, 200
        else:
            resp["message"] = "Course " + code + " not in Wishlist"
            return resp, 400

# class UserWishlistMinorCheck(Resource):
#     def get(self):
#         username = request.args.get("username")
#         try:
#             wl = Wishlist.get(username)
#             courses = [c.code for c in wl.course]
#             check = Minor.check(courses)
#             resp = jsonify({"minorCheck": check})
#             resp.status_code = 200
#             return resp
#         except Exception as e:
#             resp = jsonify({"error": "something went wrong"})
#             resp.status_code = 400
#             return resp

#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument("username", required=True)
#         data = parser.parse_args()
#         username = data["username"]
#         try:
#             wl = User.get(username)
#             courses = [c.code for c in wl.course]
#             check = Minor.check(courses)
#             resp = jsonify({"minorCheck": check})
#             resp.status_code = 200
#             return resp
#         except Exception as e:
#             resp = jsonify({"error": "something went wrong"})
#             resp.status_code = 400
#             return resp
