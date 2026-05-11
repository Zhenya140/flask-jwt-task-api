from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models import User
from app.extensions import db

auth = Blueprint("auth", __name__)

# LOGIN
@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data["username"]).first()

    if user and user.check_password(data["password"]):
        token = create_access_token(identity=str(user.id))
        return jsonify({"token": token})

    return jsonify({"error": "bad credentials"}), 401

# REGISTER
@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"msg": "missing data"}, 400

    if User.query.filter_by(username=username).first():
        return {"msg": "user already exists"}, 409

    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return {"msg": "created"}, 201