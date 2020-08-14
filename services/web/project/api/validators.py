from marshmallow import Schema, fields, validate


# validator for campground json
class CampgroundValidator(Schema):
	campground_name = fields.String(required=True)
	park = fields.String(required=True)


# validator for user json
class UserValidator(Schema):
	email = fields.Email(required=True)
	phone_number = fields.String(required=False)
	active = fields.Boolean(required=False)


# validator for reservations
class ReservationValidator(Schema):
	date = fields.Date(format='iso', required=True)
	campground_id = fields.Integer(required=True)
	user = fields.Nested(UserValidator, required=True)

