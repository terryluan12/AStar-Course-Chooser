from mongoengine import connect
from flask_cors import CORS
from api.utils.database import sql_db
from api.routes import api

from flask import Flask, send_from_directory
import os

from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config["DEBUG"] = os.environ.get("DEBUG", default=True)
    app.config["TESTING"] = os.environ.get("TESTING", default=True)
    app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
    # Configure MongoEngine
    app.config["MONGODB_HOST"] = os.environ.get("MONGODB_HOST", default=True)
    # Configure SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", default=True
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)

    connect(host=app.config["MONGODB_HOST"])

    sql_db.init_app(app)
    with app.app_context():
        sql_db.create_all()

    api.init_app(app)

    return app