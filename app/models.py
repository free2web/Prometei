from . import db
from datetime import datetime
import config

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(14), unique=True)	
	password  = db.Column(db.String(32))
	secret = db.Column(db.String(32))
	state = db.Column(db.Integer)
	lastlogin = db.Column(db.DateTime())
class Character(db.Model):
	__tablename__ = 'characters'
	id = db.Column(db.Integer, primary_key=True)
	account_id = db.Column(db.Integer)
	name = db.Column(db.String(14), unique=True)
	job = db.Column(db.String(14))
	race = db.Column(db.Integer)
	level = db.Column(db.Integer)
	map = db.Column(db.String(32))
	x = db.Column(db.Integer)
	y = db.Column(db.Integer)
	hair = db.Column(db.Integer)
	skills = db.Column(db.LargeBinary)
	items = db.Column(db.LargeBinary)
	str = db.Column(db.Integer)
	con = db.Column(db.Integer)
	spr = db.Column(db.Integer)
	acc = db.Column(db.Integer)
	deleted = db.Column(db.Integer)
	del_date = db.Column(db.DateTime())

