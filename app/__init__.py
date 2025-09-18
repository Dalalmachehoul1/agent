from flask import Flask
from app.extensions.db import init_db
from app.blueprints.chat.routes import chat_bp
from app.blueprints.hr_tools.routes import hr_tools_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.config.Config")

    # Init DB
    init_db(app)

    # Register blueprints
    app.register_blueprint(chat_bp, url_prefix="/chat")
    app.register_blueprint(hr_tools_bp, url_prefix="/hr_tools")

    return app
