#!/usr/bin/env python
#-*- coding: UTF-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo, Optional
from wtforms import ValidationError
from ..models import User
import hashlib

class CreateAccountForm(Form):
	name = StringField(u'Имя', validators=[Required(), Length(1,16)]) 
	password = PasswordField(u'Пароль', validators=[Required(), Length(1,32)])
	secret = StringField(u'Секретное слово', validators=[Required(), Length(1,32)])
	submit = SubmitField(u'Создать')

	def validate_username(self, field):
		if field.data != self.user.name and User.query.filter_by(name=field.data).first():
			raise ValidationError(u'Аккаунт с таким именем уже существует')
class EditAccountForm(Form):
	name = StringField(u'Имя', validators=[Length(1, 16)])
	password = PasswordField(u'Пароль', validators=[Length(1, 32)])
	state = IntegerField(u'Статус. В игре == 1, оффлайн == 0')
	secret = StringField(u'Секретное слово')
	submit = SubmitField(u'Обновить')
class EditCharacterForm(Form):
	name = StringField(u'Имя', validators=[Length(1, 16)])
	job = IntegerField(u'Job')
	race = IntegerField(u'Race')
	level = IntegerField(u'Level')
	str = IntegerField(u'Str')
	con = IntegerField(u'Con')
	spr = IntegerField(u'Spr')
	acc = IntegerField(u'Acc')
	submit = SubmitField(u'Обновить')