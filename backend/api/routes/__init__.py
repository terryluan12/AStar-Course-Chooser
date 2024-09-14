from flask_restx import Api
import api.routes.Courses as Courses
import api.routes.Users as Users
import api.routes.Wishlist as Wishlist

api = Api()
api.add_resource(Users.UserRegistration, '/api/user/register')
api.add_resource(Users.UserLogin, '/api/user/login')

api.add_resource(Courses.SearchCourse, '/api/searchc')
api.add_resource(Courses.ShowCourse, '/api/course/details')
# api.add_resource(Courses.ShowCourseGraph, '/course/graph')

api.add_resource(Wishlist.UserWishlist, '/api/user/wishlist')
api.add_resource(Wishlist.UserWishlistAdd, '/api/user/wishlist/addCourse')
api.add_resource(Wishlist.UserWishlistRemove, '/api/user/wishlist/removeCourse')
api.add_resource(Wishlist.UserWishlistMinorCheck, '/api/user/wishlist/minorCheck')
