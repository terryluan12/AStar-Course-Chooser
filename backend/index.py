# this is the flask core

from api import create_app
import os


if __name__ == "__main__":
    app = create_app()
    app.run(threaded=True, port=os.environ.get("PORT", default=3001))
