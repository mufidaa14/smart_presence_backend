from flask import Blueprint, request, jsonify
from app import db
from models.attendance import Attendance

attendance_bp = Blueprint("attendance", __name__)

@attendance_bp.route("/attendance", methods=["POST"])
def add_attendance():
    data = request.json
    student_id = data["student_id"]

    attendance = Attendance(student_id=student_id)
    db.session.add(attendance)
    db.session.commit()

    return jsonify({"message": "Absensi tercatat"})
