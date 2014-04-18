from flask import render_template, flash, redirect, send_from_directory, request, abort, jsonify, url_for
from app import app, db, user_datastore
from .forms import LoginForm, NewPostForm
from .models import User, Post, Role
from .utils import get_url_from_id
from flask.ext.security.decorators import login_required
from flask.ext.security.forms import LoginForm, RegisterForm
from flask.ext.security.signals import user_registered
from flask.ext.login import current_user

import random

MAX_POSTS_RETURNED = 100

@app.context_processor
def inject_login():
    if not current_user.is_authenticated():
        form = LoginForm()
        return dict(form=form)
    return dict()

@user_registered.connect_via(app)
def user_registered_sighandler(user, app):
    user_datastore.add_role_to_user(user, user_datastore.find_role("User"))

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
                'cover': post.cover,
                'support_count': post.support_count,
                'supported': (post in current_user.supported_posts)
            })
    return "error"

@app.route('/add_post', methods = ['POST'])
@login_required
def add_post():
    data = request.get_json()
    if (data is None) or (not data['title']) or (not data['content']) or (not data['longitude']) or (not data['latitude']) or (not data['cover_id']):
        abort(404)
    new_post = Post(author=current_user._get_current_object(), title=data['title'], content=data['content'], cover=get_url_from_id(data['cover_id']), location=[data['longitude'], data['latitude']]).save()
    current_user.update(push__posts=new_post)
    return jsonify(status="Success", url=url_for('story', id=new_post.id))

@app.route('/update_post', methods = ['POST'])
@login_required
def update_post():
    data = request.get_json()
    if (data is None) or (not data['type']) or (not data['id']):
        abort(404)
    if data['type'] == 'support':
        post = Post.objects.get_or_404(id=data['id'])
        if post in current_user.supported_posts:
            return jsonify(status="Error")
        post.support_count += 1
        post.save()
        current_user.supported_posts.append(post)
        current_user.save()
        return jsonify(status="Success")
    if data['type'] == 'spam':
        post = Post.objects.get_or_404(id=data['id'])
        if post in current_user.spammed_posts:
            return jsonify(status="Error")
        post.spam_count += 1
        post.save()
        current_user.spammed_posts.append(post)
        current_user.save()
        return jsonify(status="Success")
    if data['type'] == 'delete':
        post = Post.objects.get_or_404(id=data['id'])
        if post not in current_user.posts:
            return jsonify(status="Error")
        current_user.posts.remove(post)
        current_user.save()
        post.delete()
        flash("Story successfully deleted", "success")
        return jsonify(status="Success")
    return jsonify(status="Error")


@app.route('/share')
@login_required
def share_story():
    return render_template("share.html")

@app.route('/stories')
@login_required
def user_stories():
    return render_template("stories.html")

@app.route('/story/<id>')
@login_required
def story(id):
    post = Post.objects.get_or_404(id=id)
    if post not in current_user.posts:
        abort(404)
    return render_template("story.html", post=post)

@app.route('/edit/<id>')
@login_required
def edit(id):
    post = Post.objects.get_or_404(id=id)
    if post not in current_user.posts:
        abort(404)
    return render_template("edit.html", post=post)

@app.route('/')
def index():
    images = app.config['IMAGES']
    image = random.choice(images)
    return render_template("index.html", register=RegisterForm(), image=image)

@app.route('/clear')
@login_required
def clear():
    current_user.clear_viewed_posts()
    return redirect('/')
