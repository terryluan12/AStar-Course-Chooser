# This is to prevent circular imports

from flask_mongoengine import MongoEngine

app = None
db = None

def init_app(app_):
    global app
    app = app_
    return app

def init_db(app):
    global db
    db = MongoEngine(app)
    return db