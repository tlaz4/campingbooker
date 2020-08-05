from flask import Blueprint
from flask_restx import Resource, Api
from marshmallow import ValidationError

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

	def __init__(self):
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
		post_data = request.get_json()

		try:
			validated_data = self.validator.load(post_data)
		except ValidationError as err:
			response_object = {
				'status': 'fail',
				'message': 'The posted data is not valid',
				'errors': err.messages

			}

			return response_object, 401

		email = post_data.get('email')

		db.session.add(User(email=email))
		db.session.commit()

		response_object = {
			'status': 'success',
			'message': f'{email} was added!'
		}

		return response_object, 201


class Users(Resource):
	# get a user by id
	def get(self, user_id):
		user = User.query.filter_by(id=user_id).first()
		response_object = {
			'status': 'success',
			'data' : user.to_json()
		}

		return response_object, 200



api.add_resource(Ping, '/api/users/ping')
api.add_resource(UsersList, '/api/users')
api.add_resource(Users, '/api/users/<string:user_id>')

