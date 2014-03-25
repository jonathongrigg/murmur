from app import db
from datetime import datetime

ROLE_USER = 0
ROLE_PRO_USER = 1   # Paying for mesaaging
ROLE_ADMIN = 2

class User(db.Document):
    # Todo: add messages and posts
    user_id = db.SequenceField(required=True, unique=True, primary_key=True)
    email = db.EmailField(required=True)
    role = db.IntField(required=True, choices=[ROLE_USER, ROLE_PRO_USER, ROLE_ADMIN], default=ROLE_USER)
    date_created = db.DateTimeField(required=True, default=datetime.utcnow)

    def __repr__(self):
        return '<User %d>' % (self.user_id)

class Post(db.Document):
    pass
