from flask import render_template, flash, redirect, send_from_directory, request, abort, jsonify
from app import app, db, user_datastore
from .forms import LoginForm, NewPostForm
from .models import User, Post
from flask.ext.security.decorators import login_required
from flask.ext.login import current_user

MAX_POSTS_RETURNED = 10

@app.route('/get_post', methods = ['POST'])
@login_required
def get_post():
    data = request.get_json()
    if data is None:
        abort(404)
    location = [data['longitude'], data['latitude']]
    posts = Post.objects(location__near=location).limit(MAX_POSTS_RETURNED)
    output = []
    for post in posts:
        output.append({
            'id': str(post.id),
            'author': post.author.user_id,
            'date_created': post.date_created,
            'title': post.title,
            'content': post.content,
            'view_count': post.view_count,
            'support_count': post.view_count
        })
    return jsonify(posts=output)

@app.route('/add_post', methods = ['POST'])
@login_required
def add_post():
    data = request.get_json()
    if data is None:
        abort(404)
    new_post = Post(author=current_user._get_current_object(), title=data['title'], content=data['content'], location=[data['longitude'], data['latitude']]).save()
    return jsonify(status="success")

@app.route('/')
def index():
    return render_template("index.html")
