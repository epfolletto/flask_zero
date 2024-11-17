from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256 as sha256

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default="user") # user ou admin

    def verify_password(self, password):
        return sha256.verify(password, self.password_hash)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    def __repr__(self):
        return f'<User {self.username}>'