from app import db
from datetime import datetime
from flask.ext.security import UserMixin, RoleMixin

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

class User(db.Document, UserMixin):
    # Todo: add messages
    email = db.EmailField(required=True, unique=True, max_length=255)
    password = db.StringField(required=True, max_length=255)
    user_id = db.SequenceField(required=True, unique=True, primary_key=True)
    roles = db.ListField(db.ReferenceField(Role), default=[])
    date_created = db.DateTimeField(required=True, default=datetime.utcnow)
    posts = db.ListField(db.ReferenceField('Post'))

    def __repr__(self):
        return '<User %d>' % (self.user_id)

class Post(db.Document):
    author = db.ReferenceField(User, reverse_delete_rule=db.CASCADE, required=True)
    date_created = db.DateTimeField(required=True, default=datetime.utcnow)
    content = db.StringField(required=True)
    location = db.PointField(required=True)
    view_count = db.IntField(required=True, default=0)
    support_count = db.IntField(required=True, default=0)

    def __repr__(self):
        return '<Post by %d>' % (self.author)
