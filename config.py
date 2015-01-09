#!/usr/bin/env python
#-*- coding: UTF-8 -*-
"""Config file"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

#### Site settings
showOnline = True #Count and show current online on index page
deleteAccountOption = True #Allow account deletion
deleteCharacterOption = True #Allow character deletion
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