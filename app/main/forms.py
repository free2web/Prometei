#!/usr/bin/env python
#-*- coding: UTF-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo, Optional
from wtforms import ValidationError
from ..models import User, Character
import hashlib
import config

class CreateAccountForm(Form):
	name = StringField('Username', validators=[Required(), Length(1,16)]) 
	password = PasswordField('password', validators=[Required(), Length(1,32)])
	secret = StringField('Secret word', validators=[Required(), Length(1,32)])
	submit = SubmitField('Create')

	def validate_name(self, field):
		if User.query.filter_by(name=field.data).first():
			raise ValidationError('User already exists')
class EditAccountForm(Form):
	name = StringField('Username', validators=[Length(1, 16)])
	#password = PasswordField('Password', validators=[Length(1, 32)])
	state = IntegerField('Status. Online == 1, Offline == 0')
	secret = StringField('Secret word(md5)')
	if config.useMasterKey == True:
		master_key = StringField('Master key', validators=[Required()])
	submit = SubmitField('Update')

	def validate_master_key(self, field):
		master_key = field.data
		if master_key != config.master_key:
			raise ValidationError('Wrong master key')
class EditCharacterForm(Form):
	account_id = StringField('Account ID', validators=[Required(), Length(1, 16)])
	name = StringField('Name', validators=[Length(1, 16)])
	race = IntegerField('Race')
	level = IntegerField('Level')
	if config.useMasterKey == True:
		master_key = StringField('Master key', validators=[Required()])
	submit = SubmitField('Update')
	
	def validate_master_key(self, field):
		master_key = field.data
		if master_key != config.master_key:
			raise ValidationError('Wrong master key')
class CreateCharacterForm(Form):
	account_id = StringField('Account ID', validators=[Required(), Length(1, 16)])
	name = StringField('Name', validators=[Required(), Length(1, 16)])
	race = IntegerField('Race', validators=[Required()])
	level = IntegerField('Level', validators=[Required()])
	submit = SubmitField('Create')

	def validate_name(self, field):
		if Character.query.filter_by(name=field.data).first():
			raise ValidationError('Already exists')