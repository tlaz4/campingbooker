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
		campground = Campground.query.filter_by(id=campground_id).first()

		response_object = {
			'status': 'success',
			'data': campground.to_json()
		}

		return response_object, 200


api.add_resource(Campgrounds, '/api/campgrounds/<campground_id>')