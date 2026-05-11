from flask import Flask
from app.extensions import db, jwt
from config import Config

from app.api.routes import api
from app.auth.routes import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(api, url_prefix="/api")

    return app