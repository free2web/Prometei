#!/usr/bin/env python
#-*- coding: UTF-8 -*-
from datetime import datetime
from flask import render_template, session, redirect, url_for, abort, g, current_app, flash, request
from . import main
from .. import db
from ..models import User, Character
from .forms import CreateAccountForm, EditAccountForm, EditCharacterForm
import hashlib

@main.route('/', methods=['GET', 'POST'])
def index():
	users = User.query.all()
	return render_template('index.html', users=users)
@main.route('/create', methods=['GET', 'POST'])
def create_account():
	form = CreateAccountForm()
	if form.validate_on_submit():
		newAccount = User(name=form.name.data, password=hashlib.md5(form.password.data).hexdigest(), 
			secret=hashlib.md5(form.secret.data).hexdigest(), state = 0)
		
		db.session.add(newAccount)		
		db.session.commit()
		flash(u'Аккаунт создан!')
		return redirect(url_for('.index'))
	
	return render_template('create.html', form=form)
@main.route('/characters')
def characters():
	characters = Character.query.all()
	return render_template('characters.html', characters=characters)

@main.route('/editaccount/<int:id>', methods=['GET', 'POST'])
def edit_account(id):
	user = User.query.get_or_404(id)
	form = EditAccountForm(user=user)
	if form.validate_on_submit():
		user.name = form.name.data
		user.password = hashlib.md5(form.password.data).hexdigest()
		user.state = form.state.data
		user.secret = hashlib.md5(form.secret.data).hexdigest()
		db.session.add(user)
		db.session.commit()
		flash(u'Профиль пользователя успешно обновлен')
		return redirect(url_for('.index'))
	return render_template('edit_account.html', form=form, user=user)
@main.route('/editchar/<int:id>', methods=['GET', 'POST'])
def edit_character(id):
	character = Character.query.get_or_404(id)
	form = EditCharacterForm(character=character)
	if form.validate_on_submit():
		character.name = form.name.data
		character.job = form.job.data
		character.race = form.race.data
		character.level = form.level.data
		character.str = form.str.data
		character.con = form.con.data
		character.spr = form.spr.data
		character.acc = form.acc.data

		db.session.add(character)
		db.session.commit()
		flash(u'Профиль пользователя успешно обновлен')
		return redirect(url_for('.index'))
	return render_template('edit_char.html', form=form, character=character)