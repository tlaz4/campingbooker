from project import db

# table to represent users
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    phone_number = db.Column(db.String(10))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    reservations = db.relationship('Reservation', backref='user', lazy=True)

    def to_json(self):
    	return {
    		'id': self.id,
    		'email': self.email,
            'reservations': [reservation.to_json() for reservation in self.reservations]
    	}

# table to represent a campground
class Campground(db.Model):
    __tablename__ = 'campgrounds'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    campground_name = db.Column(db.String(128), unique=True, nullable=False)
    park = db.Column(db.String(128), nullable=False)

    reservations = db.relationship('Reservation', backref='campground', lazy=True)

    def to_json(self):
        return {
            'id': self.id,
            'campground_name': self.campground_name,
            'park': self.park
        }

# reservations table, foreign keys reference user and campground
# note date is isoformat YYYY-MM-DD
class Reservation(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    campground_id = db.Column(db.Integer, db.ForeignKey('campgrounds.id'), nullable=False)


    def to_json(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'campground': self.campground.to_json()
        }