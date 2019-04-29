from flask import Blueprint, render_template, abort, jsonify, request
from datetime import datetime
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
import app_setting
import app_database

blueprint = Blueprint('User', __name__,template_folder='BlueprintArchitech/User')

@blueprint.route('/register', methods=['POST'])
def register():

	users = app_database.mongo.db.users

	first_name = request.get_json()['first_name']
	last_name = request.get_json()['last_name']
	email = request.get_json()['email']
	password = app_database.bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
	created = datetime.utcnow()

	user_id = users.insert({
		'first_name': first_name,
		'last_name': last_name,
		'email': email,
		'password': password,
		'created': created,
		})

	new_user = users.find_one({'_id':user_id})
	result = {'email' : new_user['email']+ ' registered'}

	return jsonify({'result':result})

@blueprint.route('/login', methods=['POST'])
def login():
	users = app_database.mongo.db.users
	email = request.get_json()['email']
	password = request.get_json()['password']
	result = ""

	response = users.find_one({'email':email})

	if response:
		if app_database.bcrypt.check_password_hash(response['password'],password):
			access_token = create_access_token(identity = {
				'first_name':response['first_name'],
				'last_name':response['last_name'],
				'email':response['email']
				})
			result = jsonify({"token":access_token})
		else:
			result = jsonify({"error":"Invalid Username and password"})
	else:
		result = jsonify({"result":"no result found"})
	return result

# @blueprint.route('/logout', methods=['POST'])
# def logout():
# 	respond = {'status' : 200,'msj' : 'POST CALLED'}
# 	return jsonify(respond)