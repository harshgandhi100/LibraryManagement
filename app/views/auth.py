from flask import Blueprint,jsonify,request
from app.models import user

auth_bp = Blueprint('auth',__name__,url_prefix='/auth')


@auth_bp.route('/users/all',methods=['GET'])
def allUsers():
    return jsonify(list(map(lambda m:m.__dict__,user.User.query.all())))

@auth_bp.route('/loggeduser',methods=['GET'])
def loggeduser():
    temp_user = user.User.query.filter(user.User.loggedIn == 1).all()
    return jsonify(temp_user)


@auth_bp.route('/login',methods=['POST'])
def login():
    
    username = request.form['username']
    password = request.form['password']
        
    temp_user = user.User.query.filter(user.User.username == username).first()
    if temp_user.username == username and temp_user.password == password:
        temp_user.loggedIn = 1
        user.db.session.commit()
        return jsonify({'username':username})
    else:
        return ''

@auth_bp.route('/logout',methods=['GET'])
def logout():
    temp_user = user.User.query.filter(user.User.loggedIn == 1).first()
    temp_user.loggedIn = 0
    user.db.session.commit()
    return ''