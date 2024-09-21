from api.models.User import User
from api.models.Session import Session
from flask_restx import Namespace, Resource, reqparse
from api.middleware.auth import cookie_required
from werkzeug.security import check_password_hash

api = Namespace("Session", description="Session/auth related operations")


@api.route("/session")
class SessionView(Resource):

    @api.doc(params={"username": "User's username", "password": "User's password"})
    @api.doc(
        responses={
            200: "User logged in",
            401: "Login failed",
            404: "Username Incorrect",
        }
    )
    def post(self):
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

        if check_password_hash(user.password, attemptedPassword):
            session_token = user.login()
            resp["message"] = "User Logged In"
            resp["token"] = session_token
            return resp, 200
        else:
            resp["message"] = "Login failed"
            return resp, 401

    @api.doc(
        params={
            "session_token": {
                "description": "User's current session token",
                "in": "cookie",
                "required": True,
            }
        }
    )
    @api.doc(responses={200: "User logged in", 404: "Username Incorrect"})
    @cookie_required
    def delete(self, session):
        resp = {}
        session.logOut()
        resp["message"] = "User Logged Out"
        return resp, 200
