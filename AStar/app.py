# this is the flask core

from flask import Flask
from flask_restful import Api

import config

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
# MongoDB URI
DB_URI = "mongodb+srv://Cansin:cv190499@a-star.roe6s.mongodb.net/A-Star?retryWrites=true&w=majority"
app.config["MONGODB_HOST"] = DB_URI

config.init_app(app)
config.init_db(app)

# API Endpoints
import controller
api = Api(app)
api.add_resource(controller.UserRegistration, '/user/register')
api.add_resource(controller.ShowCourse, '/course')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5444, extra_files=['app.py', 'controller.py', 'model.py'])
    # with open("test.json") as f:
    #     data = json.load(f)
    # for i in range(75):
    #     i = str(i)
    #     Course(name=data["name"][i], code=data["code"][i], description=data["description"][i], prereq=data["prereq"][i], coreq=data["coreq"][i], exclusion=data["exclusion"][i]).save()

    
