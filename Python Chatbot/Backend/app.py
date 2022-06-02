from nturl2path import url2pathname
from urllib.request import urlopen
from flask import Flask
from flask_cors import CORS


def App():
    app = Flask(__name__)
    CORS(app)

    from .routes import homepage

    app.register_blueprint(homepage, url_prefix='/')

    return app
