from marshmallow import Schema, fields, validate


# validator for campground json
class CampgroundValidator(Schema):
	id = fields.Integer(required=True)
	campground_name = fields.String(required=False)
	park = fields.String(required=False)


# validator for user json
class UserValidator(Schema):
	email = fields.Email(required=True)
	phone_number = fields.String(required=False)
	active = fields.Boolean(required=False)


# validator for reservations
class ReservationValidator(Schema):
	date = fields.Date(format="iso")
	campground = fields.Nested(CampgroundValidator, required=True)
	user = fields.Nested(UserValidator, required=True)

