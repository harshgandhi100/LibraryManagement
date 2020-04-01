from app import app
import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(app.instance_path,'data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "Khufia"