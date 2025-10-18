from flask_cors import CORS
from api.utils.database import sql_db
from api.routes import api
from urllib.parse import quote_plus

from flask import Flask
import os

from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["DEBUG"] = os.environ.get("DEBUG", default=True)
    app.config["TESTING"] = os.environ.get("TESTING", default=True)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    # Configure SQLAlchemy
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)


    sql_db.init_app(app)
    with app.app_context():
        sql_db.create_all()

    api.init_app(app)

    return app
