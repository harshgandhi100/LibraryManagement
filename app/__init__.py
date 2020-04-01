from flask import Flask,jsonify,request
from flask_cors import CORS
import app.models as models
import app.views as views
app = Flask(__name__,instance_relative_config=True)
CORS(app)
app.config.from_pyfile("config.py")
with app.app_context():
   models.init_app(app)
   views.init_app(app)
   models.db.create_all()