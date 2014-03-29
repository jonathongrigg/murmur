from flask import render_template, flash, redirect, send_from_directory, request
from app import app, db, user_datastore
from .forms import LoginForm, NewPostForm
from .models import User, Post
from flask.ext.security.decorators import login_required
from flask.ext.login import current_user

from flask.ext.security.utils import encrypt_password
import random

@app.route('/near')
@login_required
def near():
    location = [float(request.args.get('longitude', 0)), float(request.args.get('latitude', 0))]
    posts = Post.objects(location__near=location)
    return render_template("near.html", posts=posts)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/post', methods = ['GET', 'POST'])
@login_required
def add_post():
    form = NewPostForm()
    if form.validate_on_submit():
        new_post = Post(author=current_user._get_current_object(), title=form.title.data, content=form.content.data, location=[float(form.longitude.data), float(form.latitude.data)]).save()
        flash('Post added')
        return redirect('/')
    return render_template('add_post.html', form=form)
