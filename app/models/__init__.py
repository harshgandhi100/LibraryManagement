from . import user

def init_app(app):
    user.db.init_app(app)