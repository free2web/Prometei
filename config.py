#!/usr/bin/env python
#-*- coding: UTF-8 -*-
"""Config file"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

#### Site settings
showOnline = True #Count and show current online on index page
deleteAccountOption = True 	#Allow account deletion
deleteCharacterOption = True #Allow character deletion
showPasswords = True 	#Show md5 of passwords on index page
showSecrets = False 	#Show md5 of secrets on index page
useMasterKey = False 	#Use master key for editing accounts or characters
master_key = os.environ.get('MASTER_KEY') or '123456789' 	#Set master key(Windows in cmd: set MASTER_KEY=yourkey)
reserved_names = ['admin', 'administrator', 'gamemaster']	#reserved names
admins = ['Play', 'Play2']	#Admin usernames here
####

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or '\xa1>\x9e\x08!\x9e|~y$Z\xb6\x9e\x10C\xdd\x93\xde\x08f\xe8\xf8\xac\xa6'
	SQL_ALCHEMY_COMMIT_ON_TEARDOWN = True

	@staticmethod
	def init_app(app):
		pass
class DevelopmentConfig(Config):
		DEBUG = True
		SQLALCHEMY_DATABASE_URI = 'postgresql://ИмяПользователя:Пароль@localhost/ИмяБазы'
class TestingConfig(Config):
		TESTING = True
		SQLALCHEMY_DATABASE_URI = 'postgresql://ИмяПользователя:Пароль@localhost/ИмяБазы'
class ProductionConfig(Config):
		DEBUG=False
		SQLALCHEMY_DATABASE_URI = 'postgresql://ИмяПользователя:Пароль@localhost/ИмяБазы'
config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
	}