import base64
import numpy as np
import cv2
from models.student import Student

def recognize_face(base64_image):

    # convert base64 → image
    img_data = base64.b64decode(base64_image)
    np_arr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # deteksi wajah
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return {"status": "no_face"}

    # simplifikasi: anggap wajah pertama → absensi otomatis
    face = faces[0]

    # Di sini kamu akan bandingkan embedding dengan database
    # Untuk sekarang, mock saja:
    student = Student.query.first()

    return {
        "status": "success",
        "student_id": student.id,
        "student_name": student.name
    }
