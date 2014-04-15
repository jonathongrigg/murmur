import re, os

CSRF_ENABLED = True
SECRET_KEY = 'development'
MONGO_URL = os.environ.get("MONGOHQ_URL")
if MONGO_URL:
    # MONGODB_SETTINGS = {
    #         'DB': MONGO_URL.split("/")[-1],
    #         'USERNAME': re.sub(r"(.*?)//(.*?)(@hatch)", r"\2",MONGO_URL).split(':')[0],
    #         'PASSWORD': re.sub(r"(.*?)//(.*?)(@hatch)", r"\2",MONGO_URL).split(':')[1],
    #         'HOST': MONGO_URL,
    #         'PORT': 10048}
    MONGODB_SETTINGS = {
            'DB': "app24085997",
            'USERNAME': "murmurmongohq",
            'PASSWORD': "murmurmongohq*",
            'HOST': "mongodb://murmurmongohq:murmurmongohq*@oceanic.mongohq.com:10048/app24085997",
            'PORT': 10048}
else:
    MONGODB_SETTINGS = {'DB': 'murmur'}
DEBUG = True
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = "U|+-CsEh1#@:*MJ&E)3|*O8u>1onU|$u~ZTgJefXJ~u#0d$Fhs AN@Y%W=+1 nJ~"
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_TRACKABLE = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'murmur@jonathongrigg.com'
MAIL_PASSWORD = 'edgemurmurapp'
IMAGES = ['http://www.gratisography.com/pictures/82H.jpg', 'http://www.gratisography.com/pictures/81H.jpg', 'http://www.gratisography.com/pictures/79H.jpg', 'http://www.gratisography.com/pictures/80H.jpg', 'http://www.gratisography.com/pictures/78H.jpg', 'http://www.gratisography.com/pictures/77H.jpg', 'http://www.gratisography.com/pictures/75H.jpg', 'http://www.gratisography.com/pictures/76H.jpg', 'http://www.gratisography.com/pictures/73H.jpg', 'http://www.gratisography.com/pictures/74H.jpg', 'http://www.gratisography.com/pictures/72H.jpg', 'http://www.gratisography.com/pictures/71H.jpg', 'http://www.gratisography.com/pictures/69H.jpg', 'http://www.gratisography.com/pictures/70H.jpg', 'http://www.gratisography.com/pictures/67H.jpg', 'http://www.gratisography.com/pictures/68H.jpg', 'http://www.gratisography.com/pictures/65H.jpg', 'http://www.gratisography.com/pictures/66H.jpg', 'http://www.gratisography.com/pictures/63H.jpg', 'http://www.gratisography.com/pictures/64H.jpg', 'http://www.gratisography.com/pictures/62H.jpg', 'http://www.gratisography.com/pictures/61H.jpg', 'http://www.gratisography.com/pictures/60H.jpg', 'http://www.gratisography.com/pictures/59H.jpg', 'http://www.gratisography.com/pictures/57H.jpg', 'http://www.gratisography.com/pictures/58H.jpg', 'http://www.gratisography.com/pictures/56H.jpg', 'http://www.gratisography.com/pictures/30H.jpg', 'http://www.gratisography.com/pictures/55H.jpg', 'http://www.gratisography.com/pictures/54H.jpg', 'http://www.gratisography.com/pictures/52H.jpg', 'http://www.gratisography.com/pictures/53H.jpg', 'http://www.gratisography.com/pictures/51H.jpg', 'http://www.gratisography.com/pictures/50H.jpg', 'http://www.gratisography.com/pictures/49H.jpg', 'http://www.gratisography.com/pictures/48H.jpg', 'http://www.gratisography.com/pictures/47H.jpg', 'http://www.gratisography.com/pictures/46H.jpg', 'http://www.gratisography.com/pictures/44H.jpg', 'http://www.gratisography.com/pictures/45H.jpg', 'http://www.gratisography.com/pictures/43H.jpg', 'http://www.gratisography.com/pictures/42H.jpg', 'http://www.gratisography.com/pictures/41H.jpg', 'http://www.gratisography.com/pictures/40H.jpg', 'http://www.gratisography.com/pictures/38H.jpg', 'http://www.gratisography.com/pictures/39H.jpg', 'http://www.gratisography.com/pictures/36H.jpg', 'http://www.gratisography.com/pictures/37H.jpg', 'http://www.gratisography.com/pictures/35H.jpg', 'http://www.gratisography.com/pictures/33H.jpg', 'http://www.gratisography.com/pictures/26H.jpg', 'http://www.gratisography.com/pictures/34H.jpg', 'http://www.gratisography.com/pictures/32H.jpg', 'http://www.gratisography.com/pictures/28H.jpg', 'http://www.gratisography.com/pictures/31H.jpg', 'http://www.gratisography.com/pictures/23H.jpg', 'http://www.gratisography.com/pictures/25H.jpg', 'http://www.gratisography.com/pictures/27H.jpg', 'http://www.gratisography.com/pictures/24H.jpg', 'http://www.gratisography.com/pictures/hollowH.jpg', 'http://www.gratisography.com/pictures/21H.jpg', 'http://www.gratisography.com/pictures/22H.jpg', 'http://www.gratisography.com/pictures/19H.jpg', 'http://www.gratisography.com/pictures/20H.jpg', 'http://www.gratisography.com/pictures/1H.jpg', 'http://www.gratisography.com/pictures/6H.jpg', 'http://www.gratisography.com/pictures/17H.jpg', 'http://www.gratisography.com/pictures/18H.jpg', 'http://www.gratisography.com/pictures/3H.jpg', 'http://www.gratisography.com/pictures/4H.jpg', 'http://www.gratisography.com/pictures/5H.jpg', 'http://www.gratisography.com/pictures/2H.jpg', 'http://www.gratisography.com/pictures/7H.jpg', 'http://www.gratisography.com/pictures/8H.jpg', 'http://www.gratisography.com/pictures/9H.jpg', 'http://www.gratisography.com/pictures/10H.jpg', 'http://www.gratisography.com/pictures/15H.jpg', 'http://www.gratisography.com/pictures/16H.jpg', 'http://www.gratisography.com/pictures/11H.jpg', 'http://www.gratisography.com/pictures/12H.jpg', 'http://www.gratisography.com/pictures/13H.jpg', 'http://www.gratisography.com/pictures/14H.jpg']
