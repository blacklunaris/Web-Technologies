from datetime import date
from flask_sqlalchemy import SQLAlchemy
from . import db



class User(db.Model):
    __tablename__="user"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), unique=True)
    email= db.Column(db.String(120), unique=True)
    pw_hash=db.Column(db.String(80))

    
    def __init__(self, username, email,pw_hash):
        self.username= username
        self.email= email
        self.pw_hash=pw_hash

    def __repr__(self):
        return '<User%r>' % self.username

class Booking(db.Model):
    __tablename__="booking"
    id=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.String(10))
    time=db.Column(db.Integer(4))

    def __init__(self, date, time):
        self.date= date
        self.time= time

class Facility(db.Model):
    __tablename__="facility"
    id=db.Column(db.Integer, primary_key=True)
    facilityName=db.Column(db.String(80),unique=True)

