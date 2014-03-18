from flask import Flask
from flaskext.mongoalchemy import MongoAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = MongoAlchemy(app)

from app import views
