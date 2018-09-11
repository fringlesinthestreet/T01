from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    from models import db
    db.init_app(app)

    return app
