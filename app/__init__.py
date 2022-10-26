import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message
from config import mail_username, mail_password

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = '493d18cba56d77f3b1a10af73e21af17'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Emmanuel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/img'
app.config['UPLOADED_PHOTO_DEST'] = os.path.join(basedir, 'static/img')
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
EMAIL_USERNAME = "eorji452@gmail.com"
EMAIL_HOST_PASSWORD = "sqokdetbwukuwxzo"
app.config['MAIL_USERNAME'] = EMAIL_USERNAME
app.config['MAIL_PASSWORD'] = EMAIL_HOST_PASSWORD

mail = Mail(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from app.users.routes import users
from app.carts.carts import carts
from app.main.routes import main
from app.product.routes import prod
from app.blogs.routes import blogs
from app.recom.routes import recom
from app.admin.routes import admin
from app.order.routes import order
from app.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(carts)
app.register_blueprint(main)
app.register_blueprint(prod)
app.register_blueprint(blogs)
app.register_blueprint(recom)
app.register_blueprint(admin)
app.register_blueprint(order)
app.register_blueprint(errors)


