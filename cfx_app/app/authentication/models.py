from app.authentication import db
from wtforms import DateField


class UserDetails(db.Model):
    __tablename__ = 'users_details'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(
        db.String(40),
        unique=True,
        nullable=False
    )
    lastname = db.Column(
        db.String(40),
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(40),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False
    )
    social_media_type = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False)
    social_media_id = db.Column(
        db.Integer, unique=False,
        nullable=False
    )
    login_type = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False)
    stripe_customer_id = db.Column(
        db.Integer, unique=False,
        nullable=False
    )
    created_at = DateField('created_at', format='%m/%d/%Y')
    updated_at = DateField('updated_at', format='%m/%d/%Y')

    def __repr__(self):
        return '<User %r>' % self.username
