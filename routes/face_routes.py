from flask import Blueprint, request, jsonify
from services.face_service import recognize_face

face_bp = Blueprint("face", __name__)

@face_bp.route("/face-recognition", methods=["POST"])
def face_recognition():
    image_base64 = request.json.get("image")

    result = recognize_face(image_base64)
    return jsonify(result)
