from .auth import auth_bp
from flask_jwt_extended import JWTManager

jwt = JWTManager()

def init_app(app):
    app.register_blueprint(auth_bp)
    jwt.init_app(app)
