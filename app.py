from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)

    # import routes
    from routes.auth_routes import auth_bp
    from routes.student_routes import student_bp
    from routes.attendance_routes import attendance_bp
    from routes.face_routes import face_bp

    # register blueprint
    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(student_bp, url_prefix="/api")
    app.register_blueprint(attendance_bp, url_prefix="/api")
    app.register_blueprint(face_bp, url_prefix="/api")

    with app.app_context():
        db.create_all()

    return app


# run server
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
