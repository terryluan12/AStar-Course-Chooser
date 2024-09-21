import jwt
from functools import wraps
from flask import request
from flask import current_app
from api.models.Session import Session

def cookie_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        session_token = request.cookies.get("session_token")
        if not session_token:
            return {
                "message": "Unauthorized access",
            }, 401
        try:
            data=jwt.decode(session_token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            session= Session.get(data["session_id"])
            if session is None:
                return {
                "message": "Unauthorized access",
                }, 401
        except Exception as e:
            return {
                "message": "Something went wrong",
                "error": str(e)
            }, 500

        return f(session=session, *args, **kwargs)

    return decorated