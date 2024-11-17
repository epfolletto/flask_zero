from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from .models import db
from .users import users_bp
from .auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)
db.init_app(app)

app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(auth_bp, url_prefix="/auth")
