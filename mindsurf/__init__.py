# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.mail import Mail, Message
# from flask.ext.admin import Admin
from . import views


app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
# mail = Mail(app)
# admin = Admin(app, name='AutoRes')
