from flask_restx import Namespace, Resource, reqparse
from api.models.User import User
from api.middleware.auth import cookie_required
from werkzeug.security import generate_password_hash, check_password_hash

api = Namespace("Users", description="User related operations")


@api.route("/user")
class UserView(Resource):
    # TODO Remove deprecated reqparse
    @api.doc(params={"username": "User's username", "password": "User's password"})
    @api.doc(responses={201: "User created", 409: "Username already exists"})
    def post(self):
        resp = {}
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        data = parser.parse_args()
        username = data["username"]
        password = data["password"]

        if User.get(username):
            resp["message"] = "User already exists"
            return resp, 409
        else:
            User.put(username, generate_password_hash(password))
            resp["message"] = "User " + username + " created"
            return resp, 201

    @api.param(
        "session_token", "User's current session token", _in="cookie", required=True
    )
    @api.param("oldPassword", "Password to change from", required=True)
    @api.param("newPassword", "Password to change to", required=True)
    @api.doc(
        responses={
            200: "Success - Password changed",
            401: "Password Incorrect",
            404: "User not found",
        }
    )
    @cookie_required
    def patch(self):
        resp = {}
        # TODO FIX PASSWORD UPDATE
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("oldPassword", required=True)
        parser.add_argument("newPassword", required=True)
        data = parser.parse_args()
        username = data["username"]
        oldPassword = data["oldPassword"]
        newPassword = data["newPassword"]

        user = User.get(username)

        if user is None:
            resp["message"] = "User " + data["username"] + " could not be found"
            return resp, 404
        else:
            if check_password_hash(user.password, oldPassword):
                User.update(username, generate_password_hash(newPassword))
                resp["message"] = "Password Changed"
                return resp, 200
            else:
                resp["message"] = "Password Incorrect"
                return resp, 401

    @api.param(
        "session_token", "User's current session token", _in="cookie", required=True
    )
    @api.param("username", "User's username", required=True)
    @api.param("password", "User's password", required=True)
    @api.doc(
        responses={
            200: "Success - User deleted",
            401: "Password Incorrect",
            404: "User not found",
        }
    )
    @cookie_required
    def delete(self):
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
        else:
            if check_password_hash(user.password, attemptedPassword):
                User.delete(data["username"], user.password)
                resp["message"] = "User " + data["username"] + " deleted"
                return resp, 200
            else:
                resp["message"] = "Password Incorrect"
                return resp, 401
