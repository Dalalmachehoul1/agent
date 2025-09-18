from flask import Flask
from app.blueprints.users import users_bp

app = Flask(__name__)

# Enregistrer le blueprint
app.register_blueprint(users_bp, url_prefix="/users")