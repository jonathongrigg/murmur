from flask import render_template, flash, redirect, send_from_directory, request, abort, jsonify
from app import app, db, user_datastore
from .forms import LoginForm, NewPostForm
from .models import User, Post
from flask.ext.security.decorators import login_required
from flask.ext.security.forms import LoginForm, RegisterForm
from flask.ext.login import current_user

MAX_POSTS_RETURNED = 100

@app.context_processor
def inject_login():
    if not current_user.is_authenticated():
        form = LoginForm()
        return dict(form=form)
    return dict()


@app.route('/get_post', methods = ['POST'])
@login_required
def get_post():
    data = request.get_json()
    if data is None:
        abort(404)
    location = [data['longitude'], data['latitude']]
    posts = Post.objects(location__near=location).limit(MAX_POSTS_RETURNED)
    viewed_posts = current_user.viewed_posts
    for post in posts:
        if post not in viewed_posts:
            current_user.update(push__viewed_posts=post)
            post.update(inc__view_count=1)
            return jsonify({
                'id': str(post.id),
                'author': post.author.user_id,
                'date_created': post.date_created,
                'title': post.title,
                'content': post.content,
                'view_count': post.view_count,
                'support_count': post.view_count
            })
    return "error"

@app.route('/add_post', methods = ['POST'])
@login_required
def add_post():
    data = request.get_json()
    if (data is None) or (not data['title']) or (not data['content']) or (not data['longitude']) or (not data['latitude']):
        abort(404)
    new_post = Post(author=current_user._get_current_object(), title=data['title'], content=data['content'], location=[data['longitude'], data['latitude']]).save()
    current_user.update(push__posts=new_post)
    return jsonify(status="Success")

@app.route('/share')
@login_required
def share_story():
    return render_template("share.html")

@app.route('/')
def index():
    return render_template("index.html", register=RegisterForm())

@app.route('/clear')
@login_required
def clear():
    current_user.clear_viewed_posts()
    return redirect('/')
