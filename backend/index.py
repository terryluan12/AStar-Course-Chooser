# this is the flask core

from src import app
import os


if __name__ == '__main__':
    app.run(threaded=True, port=os.environ.get("PORT", default=3001))