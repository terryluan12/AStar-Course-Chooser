from flask import request
from flask_restx import Namespace, Resource, reqparse
from api.models.User import User
from api.models.Course import Course
from api.middleware.auth import cookie_required


api = Namespace("Wishlists", description="Wishlist related operations")


@api.route("/wishlist")
class WishlistView(Resource):

    @api.param(
        "session_token", "User's current session token", _in="cookie", required=True
    )
    # @api.param('username', 'User\'s username', required=True)
    @api.doc(responses={200: "Wishlist Items retrieved", 404: "User not found"})
    @cookie_required
    def get(self, session):
        resp = {}
        user = session.user
        if user is None:
            resp["message"] = "User could not be found"
            return resp, 404
        else:
            wishlistItems = user.getWishlist()
            resp["message"] = "Wishlist Items retrieved"
            resp["wishlist"] = [
                wishlistItem.to_json() for wishlistItem in wishlistItems
            ]
            return resp, 200

    @api.param(
        "session_token", "User's current session token", _in="cookie", required=True
    )
    @api.param("course_code", "Course's course code to add to wishlist", required=True)
    @api.doc(
        responses={
            200: "Course added to wishlist",
            400: "Course already in Wishlist",
            404: "User or Course not found",
        }
    )
    @cookie_required
    def post(self, session):
        resp = {}
        code = request.args.get("course_code")
        # try:
        user = session.user
        courses = Course.get(code)

        if user is None:
            resp["message"] = "User could not be found"
            return resp, 404
        elif not courses:
            resp["message"] = "Course " + code + " not found"
            return resp, 404

        if user.appendWishlist(courses):
            resp["message"] = "Course added to wishlist"
            return resp, 200
        else:
            resp["message"] = "Course " + code + " already in Wishlist"
            return resp, 400

    @api.param(
        "session_token", "User's current session token", _in="cookie", required=True
    )
    @api.param("username", "User's username", required=True)
    @api.param("course_code", "Course's course code to add to wishlist", required=True)
    @api.doc(
        responses={
            200: "Wishlist Item deleted",
            400: "Course not in Wishlist",
            404: "User or Course not found",
        }
    )
    @cookie_required
    def delete(self, session):
        resp = {}
        parser = reqparse.RequestParser()
        parser.add_argument("course_code", required=True)
        data = parser.parse_args()
        user = session.user
        course_code = data["course_code"]
        course = Course.get(course_code)

        if not user:
            resp["message"] = "User could not be found"
            return resp, 404
        elif not course:
            resp["message"] = "Course " + course_code + " not found"
            return resp, 404

        if user.removeWishlist(course):
            resp["message"] = "Removed course"
            return resp, 200
        else:
            resp["message"] = "Course " + course_code + " not in Wishlist"
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
