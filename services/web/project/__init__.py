import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
cors = CORS()

def create_app(script_info=None):
    app = Flask(__name__)

    # get config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)
    cors.init_app(app)

    # register the blueprints
    from project.api.users import users_blueprint
    from project.api.campgrounds import campground_blueprint
    app.register_blueprint(users_blueprint)
    app.register_blueprint(campground_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
