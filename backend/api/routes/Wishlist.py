from flask import jsonify, request
from flask_restx import Namespace, Resource, reqparse, fields
from api.models.Wishlist import Wishlist


api = Namespace('Wishlists', description='Wishlist related operations')

model = api.model('WishlistItem', {
    'id': fields.Integer,
    'username': fields.String,
    'course_code': fields.String,
    'course_name': fields.String,
})

@api.route('/wishlist')
class WishlistView(Resource):

    @api.doc(params={'username': 'User\'s username'})
    @api.marshal_with(model, code=200, description='Course Found')
    def get(self):
        username = request.args.get("username")
        try:
            wishlistItems = [item.to_json() for item in Wishlist.get(username)]
            resp = jsonify({"wishlist": wishlistItems})
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({"error": e})
            resp.status_code = 400
            return resp

    @api.doc(params={'username': 'User\'s username', 'course_code': 'Course Code', 'course_name': 'Course Name'})
    @api.doc(responses={ 201: 'Wishlist Item created'})
    def post(self):
        username = request.args.get("username")
        code = request.args.get("course_code")
        name = request.args.get("course_name")
        try:
            Wishlist.add_course(username, code, name)
            resp = jsonify({"wishlist": "Course added"})
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({"error": e})
            resp.status_code = 400
            return resp

    @api.doc(params={'username': 'User\'s username', 'course_code': 'Course Code'})
    @api.doc(responses={ 200: 'Wishlist Item deleted'})
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("code", required=True)
        data = parser.parse_args()
        username = data["username"]
        code = data["code"]
        try:
            Wishlist.remove_course(username, code)
            resp = jsonify({"wishlist": "removed course"})
            resp.status_code = 200
            return resp
        except Exception as e:
            resp = jsonify({"error": "something went wrong"})
            resp.status_code = 400
            return resp

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
