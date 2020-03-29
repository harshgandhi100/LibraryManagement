from flask import Flask,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from . import models
from . import views

app = Flask(__name__,instance_relative_config=True)
CORS(app)
app.config.from_object("config")
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)
models.init_app(app)
views.init_app(app)