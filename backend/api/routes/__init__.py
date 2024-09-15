from flask_restx import Api
from api.routes.Courses import CourseView
from api.routes.Users import UserView
from api.routes.Wishlist import WishlistView
from api.routes.Session import SessionView

api = Api()
api.add_resource(UserView, "/api/user")
api.add_resource(CourseView, "/api/course")
api.add_resource(WishlistView, "/api/wishlist")
api.add_resource(SessionView, "/api/session")
# api.add_resource(Courses.ShowCourseGraph, '/course/graph')
