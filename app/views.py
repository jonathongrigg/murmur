from flask import render_template, flash, redirect
from app import app, db
from .forms import LoginForm
from .models import User
import random

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for ' + form.username.data + ' with password ' + form.password.data)
        return redirect('/')
    return render_template('login.html',
        title = 'Sign in',
        form = form)

@app.route('/new')
def test():
    test1 = User(email="test"+str(random.randint(2, 100000))+"@example.com").save()
    ids = []
    for user in User.objects:
        ids.append(str(user.user_id))
    return " ".join(ids)
