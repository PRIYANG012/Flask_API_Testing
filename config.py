from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_jwt import JWT, jwt_required
from flask_jwt_extended import JWTManager, create_access_token

import logging
from rich.logging import RichHandler

class Config(object):
    """
        DATABASE CONFIGURATION STRINGS
    """

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/Testing"
                        
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 3600
    WTF_CSRF_ENABLED = True




# Initialising and configuring flask object
app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = b'\xb0\xf4\xe8\\U\x8d\xba\xb4B2h\x88\xf9\x08\xb1J'

CORS(app=app)

api = Api(app=app)

jwtmanager = JWTManager(app=app)

# Database Connection
db = SQLAlchemy(app=app)
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
bcrypt = Bcrypt(app=app)

# Logging module
logging.basicConfig(
    format="%(message)s",
    level=logging.INFO,
    handlers=[RichHandler()]
)

logger = logging.getLogger("rich")