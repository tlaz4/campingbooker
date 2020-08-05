from flask import Blueprint, request
from flask_restx import Resource, Api
from marshmallow import ValidationError
from sqlalchemy.exc import DataError

from project.api.models import User
from project.api.validators import UserValidator
from project import db

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)


class Ping(Resource):
	def get(self):
		return {
			'status': 'success',
			'message': 'pong!'
		}


class UsersList(Resource):

	def __init__(self, name):
		self.validator = UserValidator()
		super(UsersList, self).__init__()

	# get all users
	def get(self):
		users = User.query.all()

		response_object = {
			'status': 'success',
			'data': {
				'users': [user.to_json() for user in users]
			}
		}

		return response_object, 200

	# post a user
	def post(self):

		response_object = {
			'status': 'fail',
			'message': 'Invalid payload',

		}

		post_data = request.get_json()

		if not post_data:
			return response_object, 401

		# try validating the data ensuring it is correct
		try:
			validated_data = self.validator.load(post_data)
			user = User.query.filter_by(email=validated_data['email']).first()

			if not user:
				user = User(**validated_data)
				db.session.add(user)
				db.session.commit()

				response_object['status'] = 'success'
				response_object['message'] = f'{user.email} was added!'

				return response_object, 201

			else:
				response_object['message'] = 'Sorry that user already exists' 
				return response_object, 401

		except ValidationError:
			return response_object, 401


class Users(Resource):
	# get a user by id
	def get(self, user_id):
		response_object = {
			'status': 'fail',
			'message': 'User does not exist',
		}

		try:
			user = User.query.filter_by(id=user_id).first()

			if not user:
				return response_object, 404

			else:
				response_object = {
					'status': 'success',
					'data' : user.to_json()
				}

				return response_object, 200

		except (ValueError, DataError):
			return response_object, 404


api.add_resource(Ping, '/api/users/ping')
api.add_resource(UsersList, '/api/users')
api.add_resource(Users, '/api/users/<user_id>')

