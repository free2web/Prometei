from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from ..models import WebUser

class LoginForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')
class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Only nums, chars and underscores')])
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message=u'Passwords not match')])
    password2 = PasswordField('Confirm password', validators=[Required()])

    submit = SubmitField('Register')

    def validate_email(self, field):
        if WebUser.query.filter_by(email=field.data).first():
            raise ValidationError(u'Email already exists')

    def validate_username(self, field):
        if WebUser.query.filter_by(username=field.data).first():
            raise ValidationError(u'Username already in use')