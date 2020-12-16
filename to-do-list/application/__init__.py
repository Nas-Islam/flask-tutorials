from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@34.105.168.162/todolist"
app.config['SECRET_KEY'] = "YOUR_SECRET_KEY"

db = SQLAlchemy(app)

from application import routes
