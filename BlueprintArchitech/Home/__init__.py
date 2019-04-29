from flask import Blueprint, render_template, abort, jsonify, request
import app_setting

blueprint = Blueprint('Home', __name__,template_folder='BlueprintArchitech/Home')

@blueprint.route('/', methods=['GET'])
def welcome():
	respond = {'status' : 200,'msj' : 'POST CALLED'}
	return jsonify(respond)

@blueprint.route('/home', methods=['GET'])
def home():
	respond = {'status' : 200,'msj' : 'GET CALLED'}
	return jsonify(respond)