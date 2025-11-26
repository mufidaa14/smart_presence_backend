from extensions import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    class_name = db.Column(db.String(50))
    face_embedding = db.Column(db.PickleType)
