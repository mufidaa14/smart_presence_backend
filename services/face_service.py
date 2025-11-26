import base64
import numpy as np
import cv2
from models.student import Student

def recognize_face(image_base64):
    if image_base64 is None:
        return {"status": "error", "message": "Gambar tidak ditemukan"}

    # base64 → numpy array
    try:
        img_data = base64.b64decode(image_base64)
        np_arr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    except:
        return {"status": "error", "message": "Gambar tidak valid"}

    if img is None:
        return {"status": "error", "message": "Gambar gagal dibaca"}

    # deteksi wajah
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                         "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return {"status": "no_face"}

    # MOCK hasil pengenalan wajah
    student = Student.query.first()

    if student is None:
        return {"status": "error", "message": "Tidak ada data siswa"}

    return {
        "status": "success",
        "student_id": student.id,
        "student_name": student.name
    }
