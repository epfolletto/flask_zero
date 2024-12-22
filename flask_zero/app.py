from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from flask_zero.models import db
from flask_zero.routers.users import users_bp
from flask_zero.routers.auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)
db.init_app(app)

app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(auth_bp, url_prefix="/auth")

# ao usar o código abaixo, deve-se rodar "poetry run app.py"
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=4000)