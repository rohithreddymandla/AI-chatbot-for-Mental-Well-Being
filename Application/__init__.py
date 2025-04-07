from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)


app.config['SECRET_KEY'] = '97a11e34bfa61946764d81c7f35bb846'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)



from Application import routes