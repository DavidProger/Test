from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os.path as os

app = Flask(__name__)
app.config['ySQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.join(os.abspath(os.dirname(__file__)), "database.db")}'

db = SQLAlchemy(app)


class User(db.Model):
	__id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), nullable=False)
	username = db.Column(db.String(60), nullable=False)
	password = db.Column(db.String(30), nullable=False)
	age = db.Column(db.Integer, nullable=False)
	email = db.Column(db.String(100), nullable=False)

	
@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)
