from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app= Flask(__name__)
app.config['DEBUG'] = True
"""app.config['SQLALCHEMY_DATABASE_URI']='mysql://password@localhost/mydatabases'"""
app.config['SQLALCHEMY_DATABASE_URI']='mysqldb://password@localhost/mydatabases'
SQLALCHEMY_TRACK_MODIFICATIONS = True
db= SQLAlchemy(app)
from app import views