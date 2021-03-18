"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
from flask.globals import session
from app import app
from app import db
from app.models import User
from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField,Form,TextField,TextAreaField, validators,SubmitField
from wtforms.validators import InputRequired
import os
from flask_sqlalchemy import SQLAlchemy
import schedule 
import time
import requests
import threading

 


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    if not session.get('logged_in'):

        return render_template('login.html')
    else:
        return render_template('home.html')
"""
@app.route('/login',methods=['POST'])
def do_admin_login():
    if request.form['pw_hash']=='password' and request.form['username']=='admin':
        session['logged_in']==True
    else:
        flash('wrong password or username!')
        return home()"""

@app.route('/logout')
def logout():
    session['logged_in']=False
    return home()

@app.route('/test/')
def test():
    """Render website's home page."""
    POST_USERNAME = "python"
    POST_PASSWORD = "python"

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        return "Object found"
    else:
        return "Object not found " + POST_USERNAME + " " + POST_PASSWORD


    return render_template('test.html')

@app.route('/login/',methods=['POST', 'Get'])
def login():
    username=StringField('name',validators=[InputRequired()])
    pw_hash=StringField('pw_hash',validators=[InputRequired()])

    user= User(request.form['username'], request.form['pw_hash'])
    return redirect(url_for('/'))

@app.route('/profile/')
def profile():
    """Render user's profile page."""
    return render_template('profile.html')


@app.route('/booking/')
def booking():

    bookings=db.execute("SELECT * FROM Booking order by id")
    return render_template("booking.html",booking=booking)

    
"""@app.route('/users/<username>')
def show_users():
    users=db.session.query.filter_by(username=username).first_or_404()
    return render_template('show_users.html', users=users)"""

"""
@app.route('/add-user', methods=['POST'])
def add_user():
    user= User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('New user was successfully added')
    return redirect(url_for('show_users'))"""
"""
@app.route('/add-booking', methods=['POST'])
def add_booking():
    booking= Booking(request.form['booking'])
    db.session.add(booking)
    db.session.commit()
    flash('New user was successfully added')
    return redirect(url_for('show_users'))"""

def runThread(job_func, endpoint):
 job_thread = threading.Thread(target=job_func, args=(endpoint, ))
 job_thread.start()

def callEndpoint(endpoint):
 req = requests.post("http://localhost:3000"+endpoint)
 res = req.text
 status = req.status_code

schedule.every(30).minutes.do(runThread, callEndpoint, '/api/ebay/orders/get')
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.secret_key=os.urandom(12)
    app.run(debug=True, host="0.0.0.0", port="8080")
