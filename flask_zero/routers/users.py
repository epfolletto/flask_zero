from flask import Blueprint, request, jsonify
from flask_zero.models import db, User
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask_zero.schemas.user import UserCreateModel
from pydantic import ValidationError

users_bp = Blueprint('users', __name__)


@users_bp.route('/hello', methods=['GET'])
def hello():
    return{"msg": "Hello world3"}


@users_bp.route('/create', methods=['POST'])
def create_user():
    try:
        data = UserCreateModel(**request.json)
    except ValidationError as e:
        return jsonify({'errors': e.errors()}), 400

    if User.query.filter_by(username=data.username).first():
        return jsonify({"msg": "Username já está em uso"}), 409

    user = User(
        username=data.username,
        password_hash=User.generate_hash(data.password)
    )
    db.session.add(user)
    db.session.commit()

    return jsonify(
        {"message": "User created successfully"}), 201


@users_bp.route('/list', methods=['GET'])
@jwt_required()
def list_users():
    role = get_jwt().get('role')

    if role != 'admin':
        return jsonify({"msg": "Access denied!"}), 403

    users = User.query.all()

    result = [{"id": user.id, "username": user.username} for user in users]

    return jsonify(result), 201


@users_bp.route('/delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    logged_user_role = get_jwt().get('role')
    logged_user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if logged_user_role != 'admin' and user_id != logged_user_id:
        return jsonify({"error": "Unauthorized access"}), 403

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"}), 200


@users_bp.route('/update/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    logged_user_role = get_jwt().get('role')
    logged_user_id = get_jwt_identity()

    if logged_user_role != 'admin' and user_id != logged_user_id:
        return jsonify({"error": "Unauthorized access"}), 403

    data = request.json
    user = User.query.get(user_id)

    if 'username' in data:
        user.username = data['username']

    if 'password' in data:
        user.password = user.generate_hash(data['password'])

    if 'role' in data:
        if logged_user_role != 'admin':
            return jsonify({"error": "Unauthorized access"}), 403

        if data['role'] not in ['admin', 'user']:
            return jsonify({"error": "Invalid role"}), 400

        user.role = data['role']

    db.session.commit()
    return jsonify({"message": "User updated successfully"}), 200
