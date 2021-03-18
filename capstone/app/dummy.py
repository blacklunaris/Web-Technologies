from app.models import Booking
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('mysqldb:///tutorial.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin","admin@email.com","password")
session.add(user)

user = User("python","python@email.com","python")
session.add(user)

user = User("jumpiness","jump@email.com","python")
session.add(user)

booking = Booking("March 18,2021","9:00 am")
session.add(booking)

# commit the record the database
session.commit()

session.commit()