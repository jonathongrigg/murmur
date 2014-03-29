from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
    email = TextField('email', validators = [Required()])
    password = TextField('password', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class NewPostForm(Form):
    title = TextField('title', validators = [Required()])
    content = TextField('content', validators = [Required()])
    latitude = TextField('latitude', validators = [Required()])
    longitude = TextField('longitude', validators = [Required()])
