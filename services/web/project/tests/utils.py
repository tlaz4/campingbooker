from project import db
from project.api.models import User, Campground

def create_user(email):
	user = User(email=email)
	db.session.add(user)
	db.session.commit()

	return user

def create_campground(name, park):
	campground = Campground(campground_name=name, park=park)
	db.session.add(campground)
	db.session.commit()

	return campground