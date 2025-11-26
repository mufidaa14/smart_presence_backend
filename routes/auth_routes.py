from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email, password=password).first()

    if not user:
        return jsonify({"status": "error", "message": "Login gagal"}), 401

    return jsonify({
        "status": "success",
        "message": "Login berhasil",
        "role": user.role,
        "user_id": user.id
    })
