from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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
