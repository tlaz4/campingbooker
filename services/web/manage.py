import sys
import unittest
from datetime import date

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User, Campground, Reservation

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


# seed the db with some sample data
@cli.command("seed_db")
def seed_db():
    user = User(email="tlazaren@ualberta.ca")
    campground = Campground(
        campground_name="Wabasso", 
        park="Jasper National Park"
    )

    db.session.add(user)
    db.session.add(campground)
    db.session.commit()

    reservation = Reservation(
        date=date.today(),
        user_id=user.id,
        campground_id=campground.id
    )

    db.session.add(reservation)
    db.session.commit()


# run tests
@cli.command("test")
def test():
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)




if __name__ == "__main__":
    cli()
