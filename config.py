import os

class Config:
    SECRET_KEY = "smart_presence_secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
