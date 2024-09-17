from mongoengine import connect
from flask_cors import CORS
from api.utils.database import sql_db
from api.routes import api

from flask import Flask, send_from_directory
import os

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.config["DEBUG"] = os.environ.get("DEBUG", default=True)
app.config["TESTING"] = os.environ.get("TESTING", default=True)
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


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")
