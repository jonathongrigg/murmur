from flask import render_template, flash, redirect
from app import app, db, user_datastore
from .forms import LoginForm
from .models import User

from flask.ext.security.utils import encrypt_password
import random

# @app.before_first_request
# def create_user():
#     user_datastore.create_user(email='matt@nobien.net', password=encrypt_password('password'))

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for ' + form.email.data + ' with password ' + form.password.data)
#         return redirect('/')
#     return render_template('login.html',
#         title = 'Sign in',
#         form = form)

@app.route('/new')
def test():
    test1 = User(email="test"+str(random.randint(2, 100000))+"@example.com").save()
    ids = []
    for user in User.objects:
        ids.append(str(user.user_id))
    return " ".join(ids)
