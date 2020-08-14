from flask import Blueprint, request
from flask_restx import Resource, Api
from marshmallow import ValidationError
from sqlalchemy.exc import DataError

from project.api.models import Campground
from project.api.validators import CampgroundValidator
from project import db

campground_blueprint = Blueprint('campgrounds', __name__)
api = Api(campground_blueprint)

class Campgrounds(Resource):
	# get a campground by its id
	def get(self, campground_id):
		response_object = {
			'status': 'fail',
			'message': 'Campground does not exist',
		}

		try:
			campground = Campground.query.filter_by(id=campground_id).first()

			if not campground:
				return response_object, 404
			else:
				response_object = {
					'status': 'success',
					'data': campground.to_json()
				}

				return response_object, 200

		except (ValueError, DataError):
			return response_object, 404


class CampgroundList(Resource):

	def __init__(self, name):
		self.validator = CampgroundValidator()
		super(CampgroundList, self).__init__()

	def get(self):
		campgrounds = Campground.query.all()

		response_object = {
			'status': 'success',
			'data': {
				'campgrounds':	[campground.to_json() for campground in campgrounds]
			}
		}

		return response_object, 200

	# post a new campground
	def post(self):
		response_object = {
			'status': 'fail',
			'message': 'Invalid payload'
		}

		post_data = request.get_json()

		if not post_data:
			return response_object, 401
		
		try:
			validated_data = self.validator.load(post_data)
			campground = Campground.query.filter_by(campground_name=validated_data['campground_name']).first()


			if not campground:
				new_campground = Campground(**validated_data)
				db.session.add(new_campground)
				db.session.commit()

				response_object['status'] = 'success'
				response_object['message'] = f'{new_campground.campground_name} was added'

				return response_object, 201

			else:
				response_object['message'] = 'Sorry that campground already exists'
				return response_object, 401

		except ValidationError:
			return response_object, 401




api.add_resource(Campgrounds, '/api/campgrounds/<campground_id>')
api.add_resource(CampgroundList, '/api/campgrounds')