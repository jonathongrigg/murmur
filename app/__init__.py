from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.security import Security, MongoEngineUserDatastore
from flask.ext.security.forms import RegisterForm

app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)

from .models import User, Role
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore, confirm_register_form=RegisterForm)

from flask_mail import Mail
mail = Mail(app)

from app import views
