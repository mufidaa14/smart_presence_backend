from flask import Blueprint, jsonify, request
from extensions import db
from models.student import Student

student_bp = Blueprint("students", __name__)

@student_bp.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    data = []
    for s in students:
        data.append({
            "id": s.id,
            "name": s.name,
            "class_name": s.class_name
        })
    return jsonify(data)

@student_bp.route("/students", methods=["POST"])
def create_student():
    data = request.json
    student = Student(
        name=data["name"],
        class_name=data["class_name"],
        face_embedding=None
    )
    db.session.add(student)
    db.session.commit()

    return jsonify({"message": "Siswa berhasil ditambah"})
