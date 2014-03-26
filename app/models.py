from app import db
from datetime import datetime

ROLE_USER = 0
ROLE_PRO_USER = 1   # Paying for mesaaging
ROLE_ADMIN = 2

class User(db.Document):
    # Todo: add messages
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    user_id = db.SequenceField(required=True, unique=True, primary_key=True)
    role = db.IntField(required=True, choices=[ROLE_USER, ROLE_PRO_USER, ROLE_ADMIN], default=ROLE_USER)
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
