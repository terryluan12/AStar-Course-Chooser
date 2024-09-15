from flask import jsonify
from flask_restx import reqparse
from api.models.sqlModel.User import User
from flask_restx import Resource, reqparse

# -------------------- User related --------------------
class SessionView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        data = parser.parse_args()
        user = {"username": data["username"], "password": data["password"]}
        try:
            if User.verify_password(user["username"], user["password"]):
                resp = jsonify({"username": user["username"]})
                resp.status_code = 200
            else:
                resp = jsonify({"message": "Login failed"})
                resp.status_code = 401
                return resp
        except Exception as e:
            resp = jsonify({"error": e})
            resp.status_code = 400
            return resp

# ------------------------------------------------------------
