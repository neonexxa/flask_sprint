from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from BlueprintArchitech import User, Home
import app_setting
 
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = app_setting.jwtsecret
jwt = JWTManager(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

# app.register_blueprint(Home.blueprint,url_prefix='/')
app.register_blueprint(User.blueprint,url_prefix='/user')

if __name__ == "__main__":
    app.run(threaded=True,host='0.0.0.0')