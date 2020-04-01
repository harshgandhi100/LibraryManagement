from flask import Blueprint,jsonify,request,abort
from app.models.user import User,db
import jsonpickle
from flask_jwt_extended import ( jwt_required, create_access_token,
    get_jwt_identity
)

auth_bp = Blueprint('auth',__name__,url_prefix='/auth')


@auth_bp.route('/users/all',methods=['GET'])
@jwt_required
def allUsers():
    return jsonpickle.encode(User.query.all(),unpicklable=False)

@auth_bp.route('/currentuser',methods=['GET'])
@jwt_required
def currentuser():
    return jsonpickle.encode({"username":get_jwt_identity()})


@auth_bp.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    temp_user = User.query.filter(User.username == username).first()
    if temp_user.username == username and temp_user.password == password:
        access_token = create_access_token(identity=username)
        return jsonpickle.encode({"access_token":access_token},unpicklable=False),200
    else:
        #abort(401,description="Wrong username or Password")
        return jsonpickle.encode({"errmsg":"Wrong username or Password"},unpicklable=False),401

@auth_bp.route('/register',methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    temp_user = User.query.filter(User.username == username).first()
    if temp_user == None:
        new_user = User(username=username,password=password)
        db.session.add(new_user)
        db.session.commit()
        access_token = create_access_token(identity=username)
        return jsonpickle.encode({"access_token":access_token},unpicklable=False),200
    else:
        #abort(500,description="User Already Exists")
        return jsonpickle.encode({"errmsg":"User Already Exists"},unpicklable=False),500
    