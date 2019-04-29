from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

import app_setting

app = Flask(__name__)

app.config['MONGO_DBNAME'] = app_setting.dbname
app.config['MONGO_URI'] = app_setting.dburi

mongo = PyMongo(app)
bcrypt = Bcrypt(app)