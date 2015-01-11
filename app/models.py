from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import config
from flask.ext.login import UserMixin, AnonymousUserMixin
from . import login_manager

class WebUser(db.Model, UserMixin):
	__tablename__ = 'webusers'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(16), unique=True)
	password  = db.Column(db.String(32))
	email = db.Column(db.String(64), unique=True)
	password_hash = db.Column(db.String(128))
	game_account_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	@property
	def password(self):
		raise AttributeError('Password is not a readable attribute')
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)
	def __repr__(self):
		return '<User %r>' % self.username

class AnonymousUser(AnonymousUserMixin):
  def __init__(self):
    self.username = 'Guest'
login_manager.anonymous_user = AnonymousUser
@login_manager.user_loader
def load_user(user_id):
	return WebUser.query.get(int(user_id))
class User(db.Model, UserMixin):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(14), unique=True)
	children = db.relationship('WebUser', backref='account_name', lazy='dynamic')
	password  = db.Column(db.String(32))
	email = db.Column(db.String(64), unique=True)
	secret = db.Column(db.String(32))
	state = db.Column(db.Integer)
	last_login = db.Column(db.DateTime())
	

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
	agi = db.Column(db.Integer)
	spr = db.Column(db.Integer)
	acc = db.Column(db.Integer)
	deleted = db.Column(db.Integer)
	del_date = db.Column(db.DateTime())
	
