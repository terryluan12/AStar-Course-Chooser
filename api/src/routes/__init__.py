from flask_restx import Api
import src.routes.Courses as Courses
import src.routes.Users as Users
import src.routes.Wishlist as Wishlist

api = Api()
api.add_resource(Users.UserRegistration, '/user/register')
api.add_resource(Users.UserLogin, '/user/login')

api.add_resource(Courses.SearchCourse, '/searchc')
api.add_resource(Courses.ShowCourse, '/course/details')
api.add_resource(Courses.ShowCourseGraph, '/course/graph')

api.add_resource(Wishlist.UserWishlist, '/user/wishlist')
api.add_resource(Wishlist.UserWishlistAdd, '/user/wishlist/addCourse')
api.add_resource(Wishlist.UserWishlistRemove, '/user/wishlist/removeCourse')
api.add_resource(Wishlist.UserWishlistMinorCheck, '/user/wishlist/minorCheck')
