from flask import Flask
from app.blueprints.users import users_bp

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config/config.py')

    # Enregistrement des blueprints
    app.register_blueprint(users_bp)

    return app
