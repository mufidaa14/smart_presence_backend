from flask import Blueprint, request, jsonify
from services.face_service import recognize_face

face_bp = Blueprint("face", __name__)

@face_bp.route("/face-recognition", methods=["POST"])
def face_recognition():
    base64_image = request.json.get("image")

    result = recognize_face(base64_image)
    return jsonify(result)
