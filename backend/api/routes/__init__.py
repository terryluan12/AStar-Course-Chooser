from flask_restx import Api
from api.routes.Courses import api as courseNameSpace
from api.routes.Users import api as userNameSpace
from api.routes.Wishlist import api as wishListNameSpace
from api.routes.Session import api as sessionNameSpace

api = Api()

api.add_namespace(userNameSpace, "/")
api.add_namespace(courseNameSpace, "/")
api.add_namespace(wishListNameSpace, "/")
api.add_namespace(sessionNameSpace, "/")
# api.add_resource(Courses.ShowCourseGraph, '/course/graph')
