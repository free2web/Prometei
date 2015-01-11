#!/usr/bin/env python
#-*- coding: UTF-8 -*-
from datetime import datetime
from flask import render_template, session, redirect, url_for, abort, g, current_app, flash, request
from . import main
from flask.ext.login import login_user, logout_user, login_required, current_user
from .. import db
from ..models import User, Character, WebUser
from .forms import CreateAccountForm, EditAccountForm, EditCharacterForm, CreateCharacterForm, ConnectForm
import hashlib
import config
@main.route('/', methods=['GET', 'POST'])
def index():
	users = User.query.all()
	webusers = WebUser.query.all()
	if config.showOnline == True:
		online = 0
		for user in users:
			if user.state == 1:
				online += 1
	else:
		online = 'None'
	if config.showPasswords == True:
		showPasswords = True
	else:
		showPasswords = False
	if config.showSecrets == True:
		showSecrets = True
	else:
		showSecrets = False
	if current_user.is_authenticated():
		print current_user.username
	else:
		print 'Not authenticated'
	if current_user.username in config.admins:
		admin = True
	else:
		admin = False
	return render_template('index.html', users=users, online=online, admin=admin, showPasswords=showPasswords, showSecrets=showSecrets, webusers=webusers)
@main.route('/create', methods=['GET', 'POST'])
def create_account():
	if current_user.username in config.admins:
		admin = True
	else:
		admin = False
	form = CreateAccountForm()
	if form.validate_on_submit():
		newAccount = User(name=form.name.data, password=hashlib.md5(form.password.data).hexdigest(), 
			secret=hashlib.md5(form.secret.data).hexdigest(), state = 0)
		
		db.session.add(newAccount)		
		db.session.commit()
		flash(u'Account created!')
		return redirect(url_for('.index'))
	
	return render_template('create.html', form=form, admin=admin)
@main.route('/create-char', methods=['GET', 'POST'])
def create_char():
	if current_user.username in config.admins:
		admin = True
	else:
		admin = False
	form = CreateCharacterForm()
	if form.validate_on_submit():
		newChar = Character(account_id=form.account_id.data, name=form.name.data, job=0, race=form.race.data, level=form.level.data, map="Argent City", 
			x=217000, y=278100, hair=2247, str=1, agi=1, con=1, spr=1, acc=1, deleted=0)
		db.session.add(newChar)
		db.session.commit()
		flash('Character created!')
		return redirect(url_for('.index'))
	return render_template('char_create.html', form=form, admin=admin)
@main.route('/characters')
def characters():
	characters = Character.query.all()
	users = User.query.all()
	return render_template('characters.html', characters=characters, users=users)

@main.route('/editaccount/<int:id>', methods=['GET', 'POST'])
def edit_account(id):
	user = User.query.get_or_404(id)
	form = EditAccountForm(user=user)
	if form.validate_on_submit():
		
		user.name = form.name.data
		#user.password = hashlib.md5(form.password.data).hexdigest()
		user.state = form.state.data
		user.secret = hashlib.md5(form.secret.data).hexdigest()
		db.session.add(user)
		db.session.commit()
		flash('Profile updated')
		print config.master_key
		return redirect(url_for('.index'))

	form.name.data = user.name
	form.state.data = user.state
	if config.showSecrets == True:
		form.secret.data = user.secret
	else:
		form.secret.data = 'Secret hided, check your config file'
	return render_template('edit_account.html', form=form, user=user)
@main.route('/editchar/<int:id>', methods=['GET', 'POST'])
def edit_character(id):
	character = Character.query.get_or_404(id)
	form = EditCharacterForm(character=character)
	if form.validate_on_submit():
		if form.master_key.data == config.master_key:
			character.account_id = form.account_id.data
			character.name = form.name.data
			character.job = 0
			character.race = form.race.data
			character.level = form.level.data
			character.str = 1
			character.agi = 1
			character.con = 1
			character.spr = 1
			character.acc = 1
			db.session.add(character)
			db.session.commit()
			flash(u'Character updated')
			return redirect(url_for('.characters'))

	form.account_id.data = character.account_id
	form.name.data = character.name
	form.race.data = character.race
	form.level.data = character.level
	return render_template('edit_char.html', form=form, character=character)
@main.route('/delete/character/<int:id>', methods=['GET', 'POST'])
def delete_character(id):
	if config.deleteCharacterOption == True:
		character=Character.query.get_or_404(id)
		db.session.add(character)
		db.session.delete(character)
		db.session.commit()
		flash('Success.')
		return redirect(url_for('main.characters'))
	else:
		flash('Not allowed. Check config file.')
		return redirect(url_for('main.characters'))
@main.route('/delete/account/<int:id>', methods=['GET', 'POST'])
def delete_account(id):
	if config.deleteAccountOption == True:
		account=User.query.get_or_404(id)
		db.session.add(account)
		db.session.delete(account)
		db.session.commit()
		flash('Success.')
		return redirect(url_for('main.index'))
	else:
		flash('Not allowed. Check config file.')
		return redirect(url_for('main.index'))
@main.route('/connect', methods=['GET', 'POST'])
@login_required
def connect():
	form = ConnectForm()
	if form.validate_on_submit():
		web_user = WebUser.query.filter_by(username=current_user.username).first()
		game_user = User.query.filter_by(name=form.game_account_id.data).first()
		
		if web_user and game_user is not None and hashlib.md5(form.game_account_password.data).hexdigest() == game_user.password:
			
			web_user.game_account_id = game_user.id
			db.session.add(web_user)
			db.session.commit()
			flash('Success')
			return redirect(url_for('main.index'))
		flash('wrong username or password')
	return render_template('connect.html', form=form)
@main.route('/my-characters')
@login_required
def user_characters():
	characters = Character.query.filter_by(account_id=current_user.game_account_id).all()
	return render_template('user_chars.html', characters=characters)
