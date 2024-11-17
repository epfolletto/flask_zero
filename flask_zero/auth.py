from flask import Blueprint, request, jsonify
from .models import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return jsonify({"msg": "Credenciais inválidas"}), 401

    access_token = create_access_token(identity=user.id, additional_claims={'role': user.role})
    return jsonify(access_token=access_token), 200