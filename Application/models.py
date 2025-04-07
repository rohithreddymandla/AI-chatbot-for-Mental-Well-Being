from Application import app,db,login_manager,bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    numbers = db.relationship('Emergency', backref='user', lazy=True)


    def get_id(self):
        return (self.userid)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.role}')"

class Emergency(db.Model):
    phoneid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("user.userid"), nullable=False)
    number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"User('{self.phoneid}', '{self.userid}', '{self.number}')"