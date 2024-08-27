import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
# from app.config import config
from app.config import mail_username, mail_password

app = Flask(__name__)
application = app
# app.config.from_object(config)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = '493d18cba56d77f3b1a10af73e21af17'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Emmanuel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/img'
app.config['UPLOADED_PHOTO_DEST'] = os.path.join(basedir, 'static/img')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'                                       
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'eorji452@gmail.com'
EMAIL_HOST_PASSWORD = 'jvxc grdl hofw sskv'


DEFAULT_FROM_EMAIL = '<anything you want>'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

EMAIL_USERNAME = "eorji452@gmail.com"
EMAIL_HOST_PASSWORD = "jvxc grdl hofw sskv"
app.config['MAIL_USERNAME'] = EMAIL_USERNAME
app.config['MAIL_PASSWORD'] = EMAIL_HOST_PASSWORD


mail = Mail(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# db = SQLAlchemy()
# login_manager = LoginManager()
# login_manager.login_view = "users.login"
# login_manager.login_message_category = 'info'
# bcrypt = Bcrypt()
# mail = Mail()


# def create_app(config_class=config):
#     app = Flask(__name__)
#     app.config.from_object(config)

#     db.init_app(app)
#     bcrypt.init_app(app)
#     login_manager.init_app(app)
#     mail.init_app(app)

from app.users.routes import users
from app.posts.routes import posts
from app.admin.routes import admin
from app.main.routes import main
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(admin)
app.register_blueprint(main)


# return app
