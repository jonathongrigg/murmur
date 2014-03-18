from app import db

ROLE_USER = 0
ROLE_PRO_USER = 1   # Paying for mesaaging
ROLE_ADMIN = 2

class User(db.Document):
    user_id = db.IntField(min_value = 0)
    email = db.StringField()
    role = db.EnumField(IntField(), ROLE_USER, ROLE_PRO_USER, ROLE_ADMIN)

    # Todo: add messages and posts

    def __repr__(self):
        return '<User %d>' % (self.user_id)
