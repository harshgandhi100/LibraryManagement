from flask import Flask,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(50),unique=True, nullable=False)
    loggedIn = db.Column(db.Integer, default=0, unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username
    def serialize(self):
        return {
            "username":self.username,
            "password":self.password,
            "loggedIn":self.loggedIn
        }

@app.route('/users/all',methods=['GET'])
def allUsers():
    return jsonify([User.query.first().serialize()])

@app.route('/loggeduser',methods=['GET'])
def loggeduser():
    user = User.query.filter(User.loggedIn == 1).first()
    if user == None:
        return jsonify({'username':''})
    else:
        return jsonify({'username':user.username})


@app.route('/login',methods=['POST'])
def login():
    
    username = request.form['username']
    password = request.form['password']
        
    user = User.query.filter(User.username == username).first()
    if user.username == username and user.password == password:
        user.loggedIn = 1
        db.session.commit()
        return jsonify({'username':username})
    else:
        return ''

@app.route('/logout',methods=['GET'])
def logout():
    user = User.query.filter(User.loggedIn == 1).first()
    user.loggedIn = 0
    db.session.commit()
    return ''


if __name__ == "__main__":
    app.run()