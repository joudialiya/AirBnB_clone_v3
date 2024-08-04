#!/usr/bin/python3
"""app endpoint"""

from flask import Flask
from models import storage
from api.v1.views import app_view
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_view)


if __name__ == "__main__":
    HOST = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else "0.0.0.0"
    PORT = getenv("HBNB_API_PORT") if getenv("HBNB_API_PORT") else "5000"

    app.run(host=HOST, port=PORT, threaded=True)
