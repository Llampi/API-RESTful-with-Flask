from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
#from app import db
from models import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api_bp = Blueprint("api", __name__)

@api_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"msg": "Usuario ya existe"}), 400

    user = User(username=data["username"], role=data.get("role", "user"))
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "Usuario registrado"}), 201

@api_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    
    if user and user.check_password(data["password"]):
        access_token = create_access_token(identity={"id": user.id, "role": user.role})
        return jsonify(access_token=access_token)
    
    return jsonify({"msg": "Credenciales incorrectas"}), 401

@api_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"msg": "Acceso permitido", "user": current_user})

@api_bp.route("/admin", methods=["GET"])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"msg": "Acceso denegado"}), 403
    
    return jsonify({"msg": "Bienvenido, Admin!"})
