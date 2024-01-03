# this is the flask core

from flask import Flask, send_from_directory
from flask_restful import Api
import os

from dotenv import load_dotenv
load_dotenv()

import config as config
import controller as controller

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get("DEBUG", default=True)
app.config['TESTING'] = os.environ.get("TESTING", default=True)
# MongoDB URI
app.config["MONGODB_HOST"] = os.environ.get("DB_HOST")

config.init_app(app)
config.init_db(app)
config.init_cors(app)

# API Endpoints
api = Api(app)
api.add_resource(controller.UserRegistration, '/user/register')
api.add_resource(controller.UserLogin, '/user/login')

api.add_resource(controller.SearchCourse, '/searchc')
api.add_resource(controller.ShowCourse, '/course/details')
api.add_resource(controller.ShowCourseGraph, '/course/graph')

api.add_resource(controller.UserWishlist, '/user/wishlist')
api.add_resource(controller.UserWishlistAdd, '/user/wishlist/addCourse')
api.add_resource(controller.UserWishlistRemove, '/user/wishlist/removeCourse')
api.add_resource(controller.UserWishlistMinorCheck, '/user/wishlist/minorCheck')

@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(threaded=True, port=os.environ.get("PORT", default=5000))
    
    
